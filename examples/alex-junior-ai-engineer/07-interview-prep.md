# Completed interview preparation

**Fictional teaching answers, not a real interview transcript.** All questions and answers are in English. They use [F01–F11](01-career-facts.md) and the [work sample](project/README.md). No score or interviewer feedback is invented.

## 1. Walk me through your retrieval project.

I load four synthetic FAQ records from JSON. I tokenise the query and each record, remove a small stopword set and rank records by the number of shared tokens. I break ties by document ID so the result is deterministic. If the top record has fewer than two shared tokens, I return no match. The result is the exact source text, not a generated answer. This is a small personal baseline, not a commercial AI system. [F06–F07]

## 2. Is this a RAG application?

Not yet. It implements a simple retrieval component. There is no embedding model, vector store or language-model generation. A future RAG experiment could retrieve context and pass it to a model, but that would introduce separate work on grounding, prompt boundaries, cost and evaluation. I would not describe the current project as deployed RAG. [F06–F09]

## 3. How did you evaluate it, and what remains unknown?

I authored six review queries: four basic matches, an unrelated query and a synonym case. The synonym case shows a known limitation: “forgotten credentials” has little overlap with the password record. These examples help explain expected behaviour; they do not establish overall accuracy on real user traffic. I would first collect a representative, appropriately authorised query set before comparing methods. [F08–F09]

## 4. Why is the no-match rule insufficient as a safety control?

A minimum overlap rule can reject unrelated words, but shared words can still retrieve an irrelevant record. It does not understand negation or whether the source is correct. I would log and review error categories in an authorised experiment and consider a relevance check. Those are proposed improvements, not capabilities already implemented. [F07–F09]

## 5. Explain your SQL experience without overstating it.

My support work uses approved read-only queries to group tickets by category for an internal review. I do not administer the database. A synthetic illustration would be `SELECT category, COUNT(*) FROM sample_tickets GROUP BY category;`. I would confirm the reporting period, category definitions and treatment of missing categories before interpreting the output. I would not disclose an employer's schema or customer records. [F04]

## 6. Describe a responsibility from support that transfers to engineering.

In this fictional role, I reproduce account-access or document-import problems, record the steps and pass unresolved cases to engineers. The transferable part is making a failure reproducible and preserving context for the next person. The supplied facts do not contain a particular incident or measured resolution outcome, so I would not invent a STAR success story. To prepare a real behavioural example, I would add a genuine incident and its result to the facts source first. [F03]

## 7. Have you used Docker or an agent framework?

Only as reading topics in this case. I have not packaged this project with Docker or implemented a LangGraph workflow. I can explain that they are learning gaps, and I would present completed implementation evidence before adding them as hands-on skills. [F11]

## 8. Why are you applying for a junior role?

The fictional JD accepts personal-project evidence and work under an experienced engineer. My project gives me a concrete baseline to explain, while support work contributes investigation and communication habits. I still need experience with model integration and business AI delivery. I am applying to learn those responsibilities at an appropriate level, not claiming prior production AI ownership. [F02–F11; fictional JD]

## Rehearsal plan — not yet performed

Explain the project in two minutes, run the two documented demo queries, then ask a reviewer to challenge the ranking rule and the limits of the evidence. Record actual feedback only after the rehearsal. There is no rehearsal result yet.
