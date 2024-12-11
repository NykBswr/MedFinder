def reciprocal_rank_fusion(semantic_rank, lexical_rank, k):

  for rank, (key, value) in enumerate(semantic_rank.items()):
    score = 1 / (rank + 60)
    semantic_rank[key] = {"value": value, "score": score}

  for rank, (key, value) in enumerate(lexical_rank.items()):
    score = 1 / (rank + 60)
    lexical_rank[key] = {"value": value, "score": score}

  summed_scores_dict = {}

  for key in set(semantic_rank.keys()) | set(lexical_rank.keys()):
      score1 = semantic_rank.get(key, {'score': 0})['score']
      score2 = lexical_rank.get(key, {'score': 0})['score']

      summed_score = score1 + score2

      summed_scores_dict[key] = {'score': summed_score}

  reciprocal_rank_fusion = dict(sorted(summed_scores_dict.items(), key=lambda item: item[1]['score'], reverse=True))

  return reciprocal_rank_fusion