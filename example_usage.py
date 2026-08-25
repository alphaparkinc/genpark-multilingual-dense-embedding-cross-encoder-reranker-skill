from client import MultilingualDenseEmbeddingCrossEncoderRerankerClient

def main():
    client = MultilingualDenseEmbeddingCrossEncoderRerankerClient()
    res = client.rerank_candidate_passages('Enterprise SOC2 compliance automated controls')
    print('Rerank Job: ' + res['rerank_job_id'] + ' | Top Score: ' + str(res['top_relevance_score']))
    print('Top Doc Index: ' + str(res['top_ranked_document_index']) + ' (Latency: ' + str(res['cross_encoder_latency_ms']) + 'ms)')
    print('Supported Languages: ' + str(res['supported_languages_count']) + ' | RAG Hallucination Drop: -' + str(res['rag_hallucination_reduction_pct']) + '%')

if __name__ == '__main__':
    main()
