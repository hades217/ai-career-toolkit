# Offline FAQ retrieval baseline

This is the runnable work sample used in the fictional career case. It is a small lexical baseline, **not** a production RAG system, a deployed AI service or a simulation of a paid model call. The FAQ is synthetic. No package installation, key, model, network connection or database is required. Use Python 3.9+.

From the repository root:

```sh
python3 examples/alex-junior-ai-engineer/project/faq_search.py "reset my password"
python3 examples/alex-junior-ai-engineer/project/faq_search.py "orbital mechanics"
```

The first query returns `status=matched`, `document_id=faq-access` and the exact source text. The second returns `status=no_match` with no invented answer. The terminal displays the complete result; nothing is uploaded or saved.

## Design

1. Load four local FAQ records.
2. Tokenise the query and documents, remove a small stopword set, and count overlapping tokens.
3. Sort by overlap and then by stable document ID.
4. Return the best source only when at least two tokens overlap; otherwise abstain.

The count is not a probability or an ATS/career score. Two tokens is a deliberately simple demonstration rule, not a calibrated safety threshold. Synonyms, spelling variants, negation and context can fail. A lexical match can still be irrelevant. The script does not prove factual correctness, answer quality, privacy enforcement or readiness for real customers.

## Review cases

| Query | Expected result | Purpose |
|---|---|---|
| reset my password | faq-access | Basic document retrieval |
| supported upload formats | faq-upload | Match document-format wording |
| sensitive customer data | faq-privacy | Retrieve the privacy record |
| resume export copies | faq-export | Retrieve export guidance |
| orbital mechanics | no_match | Abstain on unrelated words |
| forgotten credentials | no_match | Show the synonym limitation |

These are small, authored review cases, not an independent benchmark. No overall accuracy claim is made. To extend the project, add representative queries first, preserve source IDs and compare a new method against this baseline.

中文说明：这是完整案例中的可运行作品，只用本地词语重合检索四条虚构 FAQ。它不会调用模型，不是生产级 RAG，不生成 PDF；查询无足够匹配时明确返回未匹配。
