#!/usr/bin/env python3
"""Offline lexical retrieval demo. No model, network, credentials or file writes."""
import argparse
import json
import re
from pathlib import Path
STOPWORDS = {'a','an','and','are','can','do','does','for','how','i','in','is','it','me','my','of','on','or','the','to','what','where','with'}
def tokens(text):
    return set(re.findall(r'[a-z0-9]+', text.lower())) - STOPWORDS

def search(query, documents):
    terms = tokens(query)
    ranked = sorted(((len(terms & tokens(doc['title'] + ' ' + doc['text'])), doc) for doc in documents), key=lambda item: (-item[0], item[1]['id']))
    if not ranked or ranked[0][0] < 2:
        return {'status':'no_match','document_id':None,'answer':None,'note':'No sufficiently overlapping FAQ. Ask for clarification; do not invent an answer.'}
    score, doc = ranked[0]
    return {'status':'matched','document_id':doc['id'],'title':doc['title'],'answer':doc['text'],'overlap_count':score,'note':'Exact source text retrieved by lexical overlap; not an LLM answer or a confidence score.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query')
    args = parser.parse_args()
    docs = json.loads(Path(__file__).with_name('faq.json').read_text())
    print(json.dumps(search(args.query, docs), indent=2, ensure_ascii=False))
