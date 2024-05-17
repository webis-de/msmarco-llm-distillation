#!/usr/bin/env python3
from ir_datasets.util import RequestsDownload, Cache, home_path
from ir_datasets.formats import TrecScoredDocs


def scored_docs(rank_distill_llm_run='__rankzephyr-colbert-10000-sampled-100__msmarco-passage-train-judged.run'):
    base_path = home_path() / 'rank-disti-llm'
    requests_download = RequestsDownload(f'https://zenodo.org/records/11147862/files/{rank_distill_llm_run}?download=1')
    scored_docs = TrecScoredDocs(Cache(requests_download, base_path/rank_distill_llm_run))
    
    return scored_docs

if __name__ == '__main__':
    for i in scored_docs().scoreddocs_iter():
        print(i)
