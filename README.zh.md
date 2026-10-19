# AI Career Toolkit · AI 求职工具包

[English](README.md) · [简体中文](README.zh.md)

以事实和证据为基础，完成**岗位分析、简历定制、面试准备与申请跟踪**。先查看已经做好的完整案例，再复制模板制作自己的材料。

由 [Lightman Wang](https://github.com/hades217)（[JR Academy 匠人学院](https://jracademy.ai/)创始人）维护。下方 JR Academy 与 JobPin 产品为维护者关联资源。工具包不要求账号或购买，关联链接不代表录用或求职效果保证。

## 先打开完整成果

**Alex → Junior AI Engineer 案例完全虚构。** 人物、任职、学校与岗位都是教学情境。项目代码真实可运行，但只做本地检索基线；没有真实投递、面试、业务部署或就业结果。

| 完整成果 | 可以检查什么 |
|---|---|
| [岗位定制简历](examples/alex-junior-ai-engineer/05-tailored-resume.md) | 完整英文简历，保留工作与个人项目边界 |
| [JD 与证据分析](examples/alex-junior-ai-engineer/03-jd-analysis.md) | 每条要求对应事实 ID，缺口明确保留 |
| [逐项修改依据](examples/alex-junior-ai-engineer/06-claim-traceability.md) | 修改来源及被拒绝的夸大表述 |
| [面试准备](examples/alex-junior-ai-engineer/07-interview-prep.md) | 8 道英文题、完整示例回答与证据引用 |
| [可运行作品](examples/alex-junior-ai-engineer/project/README.md) | 本地 Python 检索、原文返回和未匹配状态 |
| [申请跟踪表](examples/alex-junior-ai-engineer/08-application-tracker.csv) | 清楚标记尚未投递的示例草稿 |

回看成果背后的[事实清单](examples/alex-junior-ai-engineer/01-career-facts.md)、[虚构 JD](examples/alex-junior-ai-engineer/02-fictional-job.md)、[基准简历](examples/alex-junior-ai-engineer/04-base-resume.md)和[待执行计划](examples/alex-junior-ai-engineer/09-gap-plan.md)。[完整案例导览](examples/alex-junior-ai-engineer/README.md)。

在仓库根目录使用 Python 3.9+ 体验作品：

```sh
python3 examples/alex-junior-ai-engineer/project/faq_search.py "reset my password"
python3 examples/alex-junior-ai-engineer/project/faq_search.py "orbital mechanics"
```

无需安装依赖、不需 key、不联网、不调用模型。第一条返回密码 FAQ，第二条明确未匹配。它不是 LLM、ATS 评估器或生产级 RAG。[实际运行输出](docs/demo-output.json)。

## 制作自己的材料

1. 把模板复制到**私有**工作目录，不把真实候选人或雇主资料提交到公开仓库。
2. 确认职业事实、目标岗位和级别。
3. 对照职责匹配证据，保留缺口与技能不确定项。
4. 从基准简历制作岗位版本，另外保存逐条修改依据。
5. 练习解释自己的工作，只记录实际发生的申请行为。

[中文工作流指南](guides/workflow.zh.md) · [English workflow guide](guides/workflow.md)

| 模板 | 用途 |
|---|---|
| [职业事实](templates/career-facts.md) | 职责、输出、完整技能清单与未知项 |
| [JD 分析](templates/jd-analysis.md) | 岗位要求、证据与缺口 |
| [证据对照 CSV](templates/evidence-matrix.csv) | 可用表格软件编辑的职责映射 |
| [基准简历](templates/base-resume.md) | 稳定内容，分清工作与个人项目 |
| [岗位简历](templates/role-resume.md) | 完整岗位版本及独立修改记录 |
| [面试准备](templates/interview-prep.md) | 有事实支撑的技术与行为经历解释 |
| [申请跟踪 CSV](templates/application-tracker.csv) | 分开保存草稿、真实行为与下一步 |

[可复制提示词](prompts/README.md)供手动放入已有对话会话使用。仓库不自动调用模型、不上传文件、不联系招聘方、不投递。题目、示例回答与解释为英文，流程指南为中英文。

## 可选求职产品：按任务分类

这里只列官方公开入口，不代表本仓库实现了相应产品功能。账号、价格和可用性以各服务为准。

| 任务 | 维护者关联资源 |
|---|---|
| 长期维护经历事实与岗位简历版本 | [求职匠 Desktop](https://jracademy.ai/tools/job-hunter) |
| 查看岗位匹配与简历工具 | [JobPin AI](https://jobpin.ai/) |
| 查找面试准备资料 | [JR Academy 面试中心](https://jracademy.ai/job-interview) |
| 自评 AI Engineer 面试准备情况 | [准备度自测](https://jracademy.ai/readiness-assessment) |
| 讨论个人职业情况 | [JR Academy 职业辅导](https://jracademy.ai/career-coaching) |

## 延伸阅读与相关目录

- [Harvard MCS：Create a Strong Resume](https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/) — 独立大学职业指南，不代表 Harvard 背书，也未复制其模板。
- [Harvard MCS：AI for Resumes and Cover Letters](https://careerservices.fas.harvard.edu/ai-resumes-and-cover-letters/) — AI 辅助求职材料的大学参考资料。
- [Awesome AI 中文版](https://github.com/hades217/awesome-ai/blob/master/README.zh.md) — 更广泛的 AI 资源。
- [Awesome AI Communities 中文版](https://github.com/hades217/awesome-ai-communities/blob/main/README.zh.md) — 按国家与城市整理的社区与交流入口。

## 范围与贡献

工具包帮助材料可追溯，不会增加本人没有的经历。不保证就业或 ATS 通过，不编造匹配百分比和面试分数。Markdown/CSV 是可编辑源文件，不是已验收的 PDF。[边界说明](docs/BOUNDARIES.md) · [核验记录](docs/REVIEW.md) · [贡献指南](CONTRIBUTING.md)。

GitHub Actions 已关闭，仓库不包含 workflow。MIT License · [LICENSE](LICENSE)。
