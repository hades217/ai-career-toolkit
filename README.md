# AI Career Toolkit

[English](README.md) · [简体中文](README.zh.md)

Evidence-first tools for **job-description analysis, resume tailoring, interview preparation and application tracking**. Use the editable templates with your own facts, or inspect the complete fictional case before starting.

Maintained by [Lightman Wang](https://github.com/hades217), founder of [JR Academy](https://jracademy.ai/). The linked JR Academy and JobPin career products are maintainer-affiliated. This repository is independently usable without an account or purchase; links do not imply a hiring outcome.

## Open the finished example

**Alex → Junior AI Engineer is entirely fictional.** The candidate, employment history, university and vacancy are invented teaching material. The project code is real and runnable, but is only an offline retrieval baseline. No application, interview, business deployment or successful job outcome is claimed.

| Finished artifact | What you can inspect |
|---|---|
| [Tailored resume](examples/alex-junior-ai-engineer/05-tailored-resume.md) | Complete English resume with accurate work/project boundaries |
| [JD-to-evidence analysis](examples/alex-junior-ai-engineer/03-jd-analysis.md) | Requirements matched to fact IDs, with gaps retained |
| [Claim and change record](examples/alex-junior-ai-engineer/06-claim-traceability.md) | Why each edit is supported and which exaggerations were rejected |
| [Interview preparation](examples/alex-junior-ai-engineer/07-interview-prep.md) | Eight English questions with full example answers and evidence references |
| [Runnable work sample](examples/alex-junior-ai-engineer/project/README.md) | Offline Python retrieval, exact-source output and no-match behaviour |
| [Application tracker](examples/alex-junior-ai-engineer/08-application-tracker.csv) | A fully labelled draft that has not been submitted |

Inspect the [facts](examples/alex-junior-ai-engineer/01-career-facts.md), [fictional JD](examples/alex-junior-ai-engineer/02-fictional-job.md), [base resume](examples/alex-junior-ai-engineer/04-base-resume.md) and [proposed gap plan](examples/alex-junior-ai-engineer/09-gap-plan.md) behind those outputs. [Full case overview](examples/alex-junior-ai-engineer/README.md).

Try the work sample from the repository root with Python 3.9+:

```sh
python3 examples/alex-junior-ai-engineer/project/faq_search.py "reset my password"
python3 examples/alex-junior-ai-engineer/project/faq_search.py "orbital mechanics"
```

No dependency installation, model, key or network connection is required. The first query retrieves the password FAQ; the second returns no match. This is lexical retrieval, not an LLM, ATS evaluator or production RAG system. [Observed demo outputs](docs/demo-output.json).

## Build your own materials

1. Copy the templates into a **private** working folder; do not publish real candidate or employer data here.
2. Confirm career facts and the exact target role and level.
3. Match requirements to evidence, preserving gaps and uncertain skills.
4. Write a targeted version from a stable base and keep a separate change record.
5. Rehearse explanations, then track only actions that actually happen.

[English workflow guide](guides/workflow.md) · [中文工作流指南](guides/workflow.zh.md)

| Template | Purpose |
|---|---|
| [Career facts](templates/career-facts.md) | Confirmed responsibilities, outputs, skills and unknowns |
| [JD analysis](templates/jd-analysis.md) | Requirements, evidence and gaps |
| [Evidence matrix CSV](templates/evidence-matrix.csv) | Spreadsheet-ready requirement mapping |
| [Base resume](templates/base-resume.md) | Stable baseline with explicit work/project sections |
| [Role-specific resume](templates/role-resume.md) | Complete version plus a separate claim record |
| [Interview preparation](templates/interview-prep.md) | Evidence-supported technical and behavioural explanations |
| [Application tracker CSV](templates/application-tracker.csv) | Drafts, real actions and next steps kept separate |

[Optional copyable prompts](prompts/README.md) are plain text for an existing chat session. Nothing calls a model, uploads your files, contacts a recruiter or applies to a job automatically. Questions, sample answers and their explanations are English; workflow guidance is bilingual.

## Optional career products — by task

These are official public entry points, not capabilities implemented by this repository. Account, pricing and availability details belong to each service.

| Task | Maintainer-affiliated resource |
|---|---|
| Maintain experience facts and tailored resume versions | [Job Hunter Desktop](https://jracademy.ai/tools/job-hunter) |
| Explore job matching and resume tools | [JobPin AI](https://jobpin.ai/) |
| Find interview preparation resources | [JR Academy Interview Center](https://jracademy.ai/job-interview) |
| Review AI Engineer interview readiness | [Readiness self-assessment](https://jracademy.ai/readiness-assessment) |
| Discuss an individual career situation | [JR Academy Career Coaching](https://jracademy.ai/career-coaching) |

## Further reading and related directories

- [Harvard MCS: Create a Strong Resume](https://careerservices.fas.harvard.edu/resources/create-a-strong-resume/) — independent university guidance; no Harvard endorsement or template reproduction is implied.
- [Harvard MCS: AI for Resumes and Cover Letters](https://careerservices.fas.harvard.edu/ai-resumes-and-cover-letters/) — supplementary university guidance on AI-assisted preparation.
- [Awesome AI](https://github.com/hades217/awesome-ai) — broader AI resources.
- [Awesome AI Communities](https://github.com/hades217/awesome-ai-communities) — local communities and networking by country/city.

## Scope and contributions

This toolkit improves the traceability of materials, not a candidate's underlying experience. There is no guaranteed job, ATS pass, match percentage or interview score. Markdown/CSV files are editable sources, not verified PDF exports. [Boundaries](docs/BOUNDARIES.md) · [Review and verification](docs/REVIEW.md) · [Contributing](CONTRIBUTING.md).

GitHub Actions is disabled and no workflows are included. MIT License · [LICENSE](LICENSE).
