import json
from pathlib import Path
import tempfile
import unittest

from scripts.parameters_status import update_document


DOC = '''# Status

<!-- parameters-status:begin -->
<!-- parameters-status:end -->

<!-- parameters-status:manual:begin -->
```toml
[[model]]
id = "lab/pending"
status = "➖ 不适用"
sync = "待写入"
verified = "2026-11-06"
notes = "人工结论"
```
<!-- parameters-status:manual:end -->
'''


class ParametersStatusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "docs").mkdir()
        self.doc = self.root / "docs/status.md"
        self.doc.write_text(DOC, encoding="utf-8")
        self.write("models/lab/complete.toml", '''schema = 2
name = "Complete"
open_weights = true
release_date = "2026-01-01"

[metadata.modelatlas.parameters]
total_billion = 10
active_billion = 2
sources = ["https://example.com/complete"]
''')
        self.write("models/lab/partial.toml", '''schema = 2
name = "Partial"
open_weights = true
release_date = "2026-01-02"

[metadata.modelatlas.parameters]
active_billion = 3
sources = ["https://example.com/partial"]
''')
        self.write("models/lab/components.toml", '''schema = 2
name = "Components"
open_weights = true
release_date = "2025-01-01"

[metadata.modelatlas.parameters]
[[metadata.modelatlas.parameters.components]]
name = "Encoder"
total_billion = 1
sources = ["https://example.com/components"]
''')
        self.write("models/lab/pending.toml", '''schema = 2
name = "Pending"
open_weights = true
release_date = "2025-01-01"
''')
        self.write("models/lab/closed.toml", '''schema = 2
name = "Closed"
open_weights = false
release_date = "2026-03-01"

[metadata.modelatlas.parameters]
total_billion = 1
sources = ["https://example.com/closed"]
''')

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def rows(self):
        text = self.doc.read_text(encoding="utf-8")
        return [line for line in text.splitlines() if line.startswith("| `")]

    def test_counts_statuses_order_and_manual_override(self):
        ok, message = update_document(self.root, "docs/status.md")
        self.assertTrue(ok)
        self.assertIn("4 个开放权重模型", message)

        rows = self.rows()
        self.assertEqual(len(rows), 4)
        self.assertIn("`lab/partial`", rows[0])
        self.assertIn("⚠️ 待核实", rows[0])
        self.assertIn("`lab/complete`", rows[1])
        self.assertIn("✅ 已收集", rows[1])
        self.assertIn("`lab/components`", rows[2])
        self.assertIn("🔒 官方未披露", rows[2])
        self.assertIn("`lab/pending`", rows[3])
        self.assertIn("➖ 不适用", rows[3])
        self.assertIn("待写入", rows[3])
        self.assertIn("核验 2026-11-06；人工结论；尚无参数记录", rows[3])
        self.assertNotIn("lab/closed", "\n".join(rows))

        text = self.doc.read_text(encoding="utf-8")
        self.assertIn("| 开放权重模型总数 | 4 |", text)
        self.assertIn("| 总参数量覆盖率 | 25.0% |", text)
        self.assertIn("| 激活参数量覆盖率 | 50.0% |", text)
        self.assertIn("| 整体收集完成率 | 25.0% |", text)
        self.assertIn("| 已确定率 | 75.0% |", text)
        self.assertIn('status = "➖ 不适用"', text)
        self.assertIn('notes = "人工结论"', text)

    def test_check_detects_changes_and_dist_marks_built(self):
        update_document(self.root, "docs/status.md")
        ok, message = update_document(self.root, "docs/status.md", check=True)
        self.assertTrue(ok)
        self.assertIn("已是最新", message)

        dist = self.root / "dist/models.json"
        dist.parent.mkdir()
        dist.write_text(json.dumps({
            "lab/complete": {
                "metadata": {"modelatlas": {"parameters": {
                    "total_billion": 10,
                    "active_billion": 2,
                    "sources": ["https://example.com/complete"],
                }}}
            }
        }), encoding="utf-8")
        update_document(self.root, "docs/status.md", dist)
        rows = self.rows()
        self.assertIn("已构建", rows[1])
        self.assertIn("已入库", rows[0])

        self.write("models/lab/partial.toml", '''schema = 2
name = "Partial"
open_weights = true
release_date = "2026-01-02"

[metadata.modelatlas.parameters]
total_billion = 7
active_billion = 3
sources = ["https://example.com/partial"]
''')
        ok, message = update_document(self.root, "docs/status.md", check=True)
        self.assertFalse(ok)
        self.assertIn("需要更新", message)

    def test_unknown_manual_override_is_rejected(self):
        text = self.doc.read_text(encoding="utf-8").replace('id = "lab/pending"', 'id = "lab/missing"')
        self.doc.write_text(text, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "untracked models"):
            update_document(self.root, "docs/status.md")


if __name__ == "__main__":
    unittest.main()