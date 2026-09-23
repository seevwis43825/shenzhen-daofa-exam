# shenzhen-daofa-exam

面向深圳九年级《道德与法治》的 Agent 技能仓库。仓库包含两个用途不同的 Skill，请按任务选择，避免混用。

## 两个 Skill 的区别

| Skill | 位置 | 适用任务 | 默认成品 |
|---|---|---|---|
| `shenzhen-daofa-exam` | 仓库根目录 | 常规单元测试、模拟卷、既有试卷修订、知识点总结及时政增补 | 按考试结构组织的学生版与答案版 |
| `shenzhen-daofa-topic-training` | [`shenzhen-daofa-topic-training/`](shenzhen-daofa-topic-training/) | **专题答卷 Skill**：按单元或主题制作填空、选择和大题专项训练，强调知识全覆盖及方法迁移 | 三个可独立布置的专题、答案解析、评分点和大题模板 |

需要“填空题专题＋选择题专题＋大题专题”时，应使用 `shenzhen-daofa-topic-training`；需要一套按时间和总分组织的常规试卷时，使用根目录的 `shenzhen-daofa-exam`。

## 能做什么

- 依据教材命题，并输出学生版与答案版 Word 文档
- 审核既有试卷的教材表述、时政事实、答案、分值和排版
- 为知识点总结补充“时政摘要—教材链接—常见考法—答题关键词”专题
- 设计情境、漫画、排序、观点辨析、材料分析等训练题

它生成的是教材配套的自编训练资料，不是官方真题，也不保证未来中考试题。

## 使用

让 Agent 先阅读 [SKILL.md](SKILL.md)。它会按任务需要读取：

- [题型与版式](references/exam-format.md)
- [时政专题](references/current-affairs.md)
- [HTML 试卷模板](assets/exam-template.html)
- [构建脚本](scripts/build_exam.py)

示例：

```text
使用 shenzhen-daofa-exam，依据九上第三单元教材和最新深圳公开时政，制作一套 50 分钟的自编训练卷；包含漫画寓意题、排序题和材料题，并输出学生版与答案版。
```

## 专题答卷 Skill 使用

专题答卷 Skill 的入口是 [`shenzhen-daofa-topic-training/SKILL.md`](shenzhen-daofa-topic-training/SKILL.md)，配有独立的专题设计规范、大题模板、HTML 模板和构建脚本。

示例：

```text
使用 shenzhen-daofa-topic-training，制作九上第二单元专题答卷：包含填空题专题、选择题专题和大题专题，知识点全覆盖；答案版提供逐题解析、评分点和可迁移解题模板。
```

## 关键原则

- 教材和用户提供资料优先；每道题都要有明确教材落点。
- 时政优先采用政府、全国人大、新华社、深圳市政府等原始发布，并记录日期和来源。
- 时政服务于教材理解；答案须使用教材概念，不能只复述新闻。
- 既有文档在副本上修订，保留原稿。
- 漫画应白底黑白线描，适合 A4 黑白打印；生成原图需保留。

## 环境说明

`SKILL.md` 和 `references/` 可在多数 Agent 环境直接使用。`scripts/build_exam.py` 依赖可用的 HTML→DOCX 转换器与 `python-docx`；不同环境可能需要调整脚本中的路径或替换转换步骤。
