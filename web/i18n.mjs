// UI translations are separate from the dataset's optional descriptions.
export const messages = {
  en: {
    models: 'Models', benchmarks: 'Benchmarks', modelIntro: 'Explore model profiles and their original benchmark results.', benchmarkIntro: 'Explore evaluation definitions, methodology and reported model results.',
    searchModels: 'Search name, model ID or lab', searchBenchmarks: 'Search name, ID, category or organization', allLabs: 'All organizations', allWeights: 'All weights', allCategories: 'All categories',
    open: 'Open', closed: 'Closed', unknown: 'Unknown', newest: 'Release: newest first', oldest: 'Release: oldest first', clear: 'Clear', empty: 'No results found.', previous: 'Previous', next: 'Next',
    model: 'Model', organization: 'Organization / Lab', release: 'Release date', weights: 'Open weights', input: 'Input', output: 'Output', modalityLabels: { text: 'Text', image: 'Image', audio: 'Audio', video: 'Video', pdf: 'PDF', decision: 'Decision', embedding: 'Embedding', reranking: 'Reranking' }, context: 'Context', results: 'Benchmark results', benchmark: 'Benchmark', version: 'Version',
    category: 'Category', metric: 'Metric', unit: 'Unit', description: 'Description', score: 'Score', conditions: 'Test conditions', source: 'Source', overview: 'Overview', capabilities: 'Capabilities',
    limits: 'Limits', definition: 'Definition', methodology: 'Methodology', modelResults: 'Model results', noResults: 'No results available.', noLinks: 'No links available.', notFound: 'Page not found',
    notFoundText: 'The requested page or ID does not exist.', backModels: '← All models', resultNote: 'Original records are shown individually, not ranked. Matching a definition does not establish comparability; missing conditions are unknown.',
    matchNote: 'Only exact, unique name, explicit version and metric matches are linked to definitions.', error: 'Could not load the data. Check your connection and try again.', retry: 'Retry',
    manifestMissing: 'Release information unavailable.', dataVersion: 'Data version', published: 'Package generated', commit: 'Git commit', website: 'Official website', methodLink: 'Methodology', external: ' (opens in a new tab)',
    yes: 'Yes', no: 'No', ambiguous: 'Ambiguous', unmatched: 'Unmatched', copyId: 'Copy ID', copy: 'Copy', copied: 'Copied', copyUnavailable: 'Copy unavailable',
    modelId: 'Model ID', benchmarkId: 'Benchmark ID', family: 'Family', license: 'License', sourcesLinks: 'Sources & links', information: 'Information',
    contextWindow: 'Context window', maxInput: 'Maximum input', maxOutput: 'Maximum output', requestBytes: 'Request bytes', higherBetter: 'Higher is better', minScore: 'Min score', maxScore: 'Max score',
    loading: 'Loading data…', loadingRelease: 'Loading release information…', skip: 'Skip to content', mainNav: 'Main navigation', mobileNav: 'Mobile navigation', search: 'Search', openMenu: 'Open menu',
    sourceRepository: 'Source repository ↗', licenseLink: 'Models.dev license', jsonData: 'JSON data', searchTitle: 'Search models and benchmarks', closeSearch: 'Close search', searchPlaceholder: 'Search by name or ID', menu: 'Menu', closeMenu: 'Close menu',
    dataUnavailable: 'Data is not available yet.', searchHint: 'Search by name, ID or organization.', first50: 'showing first 50', dataExplorer: '404 / Data explorer', language: 'Language',
    themeSystem: 'System', themeLight: 'Light', themeDark: 'Dark', themeLabel: 'Theme', changeTheme: 'Change theme, current',
    countModels: n => `${n} models`, countBenchmarks: n => `${n} benchmarks`, countResults: n => `${n} results`, countRecords: n => `${n} records`, modalities: key => `${key} modalities`,
    title: 'ModelAtlas Data — AI Models & Benchmarks', metaDescription: 'Explore AI model profiles, benchmark definitions and traceable results.',
  },
  'zh-CN': {
    models: '模型', benchmarks: '评测', modelIntro: '浏览模型档案及其原始评测成绩。', benchmarkIntro: '浏览评测定义、方法及已公布的模型成绩。',
    searchModels: '搜索名称、模型 ID 或机构', searchBenchmarks: '搜索名称、ID、类别或机构', allLabs: '所有机构', allWeights: '所有权重状态', allCategories: '所有类别',
    open: '开放', closed: '未开放', unknown: '未知', newest: '发布日期：从新到旧', oldest: '发布日期：从旧到新', clear: '清除', empty: '未找到结果。', previous: '上一页', next: '下一页',
    model: '模型', organization: '机构 / 实验室', release: '发布日期', weights: '开放权重', input: '输入', output: '输出', modalityLabels: { text: '文本', image: '图片', audio: '音频', video: '视频', pdf: 'PDF', decision: '决策', embedding: '嵌入', reranking: '重排序' }, context: '上下文', results: '评测成绩', benchmark: '评测', version: '版本',
    category: '类别', metric: '指标', unit: '单位', description: '描述', score: '成绩', conditions: '测试条件', source: '来源', overview: '概览', capabilities: '能力',
    limits: '限制', definition: '定义', methodology: '评测方法', modelResults: '模型成绩', noResults: '暂无成绩。', noLinks: '暂无链接。', notFound: '页面不存在',
    notFoundText: '请求的页面或 ID 不存在。', backModels: '← 所有模型', resultNote: '原始记录逐条展示，不作排名。匹配评测定义不代表成绩可比较；未提供的条件视为未知。',
    matchNote: '仅当名称、明确版本和指标精确且唯一匹配时，才关联评测定义。', error: '无法加载数据，请检查网络连接后重试。', retry: '重试',
    manifestMissing: '发布信息不可用。', dataVersion: '数据版本', published: '数据包生成时间', commit: 'Git 提交', website: '官方网站', methodLink: '评测方法', external: '（在新标签页打开）',
    yes: '是', no: '否', ambiguous: '匹配不唯一', unmatched: '未匹配', copyId: '复制 ID', copy: '复制', copied: '已复制', copyUnavailable: '无法复制',
    modelId: '模型 ID', benchmarkId: '评测 ID', family: '系列', license: '许可证', sourcesLinks: '来源与链接', information: '信息',
    contextWindow: '上下文窗口', maxInput: '最大输入', maxOutput: '最大输出', requestBytes: '请求字节数', higherBetter: '越高越好', minScore: '最低分', maxScore: '最高分',
    loading: '正在加载数据…', loadingRelease: '正在加载发布信息…', skip: '跳至正文', mainNav: '主导航', mobileNav: '移动端导航', search: '搜索', openMenu: '打开菜单',
    sourceRepository: '源代码仓库 ↗', licenseLink: 'Models.dev 许可证', jsonData: 'JSON 数据', searchTitle: '搜索模型和评测', closeSearch: '关闭搜索', searchPlaceholder: '搜索名称或 ID', menu: '菜单', closeMenu: '关闭菜单',
    dataUnavailable: '数据尚不可用。', searchHint: '按名称、ID 或机构搜索。', first50: '显示前 50 条', dataExplorer: '404 / 数据浏览器', language: '语言',
    themeSystem: '跟随系统', themeLight: '浅色', themeDark: '深色', themeLabel: '主题', changeTheme: '切换主题，当前',
    countModels: n => `${n} 个模型`, countBenchmarks: n => `${n} 个评测`, countResults: n => `${n} 条结果`, countRecords: n => `${n} 条记录`, modalities: key => `${key} 模态`,
    title: 'ModelAtlas Data — AI 模型与评测', metaDescription: '浏览 AI 模型档案、评测定义和可追溯的成绩。',
  },
};

export function resolveLanguage(preference, languages = []) {
  if (Object.hasOwn(messages, preference)) return preference;
  for (const language of languages) {
    if (/^zh(?:-|$)/i.test(language)) return 'zh-CN';
    if (/^en(?:-|$)/i.test(language)) return 'en';
  }
  return 'en';
}

export function descriptionLocale(language, locale) {
  return language === 'zh-CN' ? locale : null;
}
