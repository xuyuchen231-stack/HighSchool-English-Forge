# HighSchool-English-Forge v0.3

高中英语通用 Agent Skill：面向中国高中英语知识体系、无答案试卷独立解析、零基础知识精讲、写作批改、教学讲义及专业 PDF 输出。结构参考 HighSchool-Chemistry-Forge，但英语侧重语境、句法、语篇证据和表达得体性。

## 使用

将 `HighSchool-English-Forge` 文件夹放入兼容 Agent Skills 的目录，确保工具可读取 `SKILL.md`、执行 Python 和制作 PDF。ChatGPT 普通聊天不能保证自动安装外部 Agent Skill；可上传本包作为资料，或在支持的 Work/Agent 环境使用。示例提示词见 `prompts/examples.md`。

## 当前进度

- 已有课程专题索引、部分基础知识完整示范、无答案试卷协议、解析教辅验收标准、写作规范及结构校验。
- **不是**所有高中英语知识点都已写完或审校完毕。`index_only` 表示只建索引，不能冒充详细讲解。
- 不含有版权限制的整本教材、历年真题库或听力录音。

## 下一阶段

逐节点扩充知识条目（定义、规则、适用语境、例句、反例、常见误区、真题式原创练习），建立跨省考试题型映射、可追溯来源、写作评分校准样例、PDF 端到端测试。

### v0.3 — Source-anchored annotated originals

Full examination outputs require the intact original, separate annotated reading passages with question-linked evidence highlighting, paragraph translation, sentence parsing and four-option reasoning. See `references/annotated-original-evidence.md`. The prior 18-page 2024 paper is not a passing benchmark because it lacks the complete original and annotations.
