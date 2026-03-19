import numpy as np

def cosine_sim(v1,v2):
    dot_product = np.dot(v1,v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    return dot_product /(norm_v1* norm_v2)

knowledge_base = {
    "Python is a versatile programming language": [0.1, 0.9, 0.3],
    "the capital of france is paris": [0.8, 0.1, 0.1], # Fixed: 0.8 instead of 0,8
    "Machine Learning uses data to make predictions": [0.2, 0.8, 0.8]
}

query_vec = [0.15,0.85,0.3]
results ={}
for text, vec in knowledge_base.items():
    score = cosine_sim(query_vec,vec)
    results[text] = score

best_match = max(results, key=results.get)
print(f"query: 'tell me about coding '")
print(f"most relevant context:{best_match} (confidence: {results[best_match]:.4f})")