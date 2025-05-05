from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

topics = [
    "Chapter 2: Fractions and Decimals",
    "Data Handling",
 "Simple Equations",
"Lines and Angles",
"The Triangles and Its Properties",
"Congruence of Triangles",
"Comparing Quantities",
"Rational Numbers",
"Practical Geometry",
"Perimeter and Area",
"Algebraic Expressions",
"Exponents and Powers",
"Symmetry",
"Visualising Solid Shapes"
]

# 🔁 Load model only once
model = SentenceTransformer('BAAI/bge-large-en-v1.5')

# ⚡ Precompute topic embeddings
topic_embeddings = model.encode(topics)

# 🎯 Core function: returns top-k matched topics
def classify_prompt(prompt, top_k=3):
    prompt_embedding = model.encode([prompt])
    similarities = cosine_similarity(prompt_embedding, topic_embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    top_topics = [topics[i] for i in top_indices]
    return top_topics
