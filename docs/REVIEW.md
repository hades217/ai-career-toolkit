# Review and verification / 核验记录

Date / 日期: **2026-10-19**, Australia/Brisbane.

## Content review

- Both READMEs open with complete fictional outputs, followed by templates and workflow instructions.
- Seven editable templates cover career facts, JD analysis, an evidence matrix, a base resume, a role variant, interview preparation and application tracking.
- The case uses stable F01–F11 fact IDs and R01–R06 / P01–P02 requirements. Employment title, dates, project nature and unknowns remain consistent between facts, base resume, targeted version and interview answers.
- The technical support role stays distinct from AI engineering experience. The personal project stays distinct from commercial AI delivery. Docker and LangGraph stay reading topics rather than fabricated implementation skills.
- Eight interview questions, answers and explanations are English. All identities, employers, qualifications and the JD are labelled fictional. The contact uses example.com; no real candidate data is included.
- The example tracker is a draft, not a submitted application. The gap plan records proposed work, not completed learning. No score, hiring result or measured commercial improvement is invented.
- These are original toolkit materials. Public reference pages are linked, not copied into a resume template or republished question bank. No product source code, private skills, candidate files or credentials were copied.

## Runnable artifact

The two commands in the README were executed locally with Python. The first returned the exact synthetic password FAQ with `status=matched`; the unrelated query returned `status=no_match` and no answer. See [complete observed outputs](demo-output.json).

The script reads local JSON and writes only terminal output. It contains no model or network integration and requires no extra packages. The six review queries are authored examples, not a representative benchmark; only the two documented demonstration commands were executed for this verification. No full CI, full build, full lint/type-check suite, cloud workflow or provider test was run.

## Public links

Official product entry pages and university reference pages were found through current public web reads/search results. A separate [scripted HTTP snapshot](link-check.json) records three HTTP 200 responses and five connection-reset/timeout results. Those network errors are preserved, not counted as successful requests. Product links are not account, installer, payment or AI-execution acceptance.

GitHub repository metadata and files are checked separately after pushing. No workflow is included; GitHub Actions must be confirmed disabled before the first push. Commits use `[skip ci]`.

## 中文说明

已核对中英文入口、完整成果、7 份模板及案例中的事实与要求 ID。支持岗位没有被改写成 AI 工程师，个人检索项目没有被写成商业 RAG，未实现的技能与未执行的计划均保留边界。

8 道题及回答、解释均为英文。人物、任职、学校、JD 全部虚构，跟踪记录为尚未投递的草稿；没有伪造就业、面试、分数或商业指标。

两条本地作品命令实际运行，一条返回 FAQ 原文，另一条返回未匹配；完整输出可打开查看。未调用模型、不需 key、不安装依赖、不写业务数据。未运行 CI、全量检查或部署。

公开入口通过官方页面或官方搜索结果核对；独立脚本检查记录了 3 个 HTTP 200 与 5 个连接中断／超时，不把失败当成功。不据链接可达宣称账号、安装、付费或 AI 执行已经验收。
