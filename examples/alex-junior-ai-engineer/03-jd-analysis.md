# Completed role and evidence analysis

**Fictional case.** Sources: [career facts](01-career-facts.md), [fictional junior JD](02-fictional-job.md). Assessment is of the case's presented evidence, not a person's ability or hiring chances.

## Positioning

The JD explicitly accepts personal projects for a junior role. Alex has adjacent support experience and a small retrieval project, with no demonstrated professional AI role or business AI deployment. The strongest positioning is a support professional moving into junior AI engineering, supported by an inspectable baseline and honest limitations.

| Requirement | Evidence | Classification | Conclusion and next clarification |
|---|---|---|---|
| R01: basic Python and unsupported input | F06–F07; local JSON loading, search function and no-match result | Personal practice | Supported at a small-script level. Not evidence of service design, concurrency or production error handling. |
| R02: bounded SQL use | F04 | Adjacent work | Scenario describes read-only ticket grouping. Ask for an anonymised query explanation; no private database should be shared. |
| R03: retrieval versus LLM application | F06–F09 | Personal practice | Baseline and limitations can be explained. Embeddings, retrieval-augmented generation and model integration are not implemented. |
| R04: evaluation cases and limits | F08–F09; six review cases | Personal practice | Small authored cases demonstrate test design thinking. No representative benchmark or quality improvement is established. |
| R05: reproduction notes and collaboration | F03 | Adjacent work | Relevant communication responsibility. Keep the original support title; do not rename it AI engineering. |
| R06: version control and documentation | F05, F07–F09 | Adjacent work + personal practice | Git is supported by documentation work; the project has readable assumptions. No ownership of a commercial release is claimed. |
| P01: Docker | F11 | Reading only | Not established. Do not write “containerised the application.” |
| P02: model API or agent workflow | F11 plus stated unknowns | Not established | No API or agent implementation. Discuss as a learning gap, not an existing skill. |

## Application decision

The case can be presented for this fictional junior role because its required tasks allow personal-project evidence. That is a positioning decision, not a prediction of shortlist, offer or eligibility. A real role requiring commercial AI delivery would need a different gap assessment.

## Changes that are justified

Lead with the retrieval project, expand the support investigation task, keep SQL scope explicit and connect each project claim to an artifact. Retain Docker and LangGraph as reading topics, not implementation experience. No new dates, employment, metrics or seniority are introduced.

## Next actions

1. Rehearse the project's ranking rule and its failure modes.
2. Explain a synthetic read-only SQL grouping example without disclosing employer data.
3. Decide whether to complete a separate Docker exercise; record it only after it has actually been done.
4. Confirm eligibility and other application details for a real opening before submission.
