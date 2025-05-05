from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
df = pd.read_excel('data/DAV_YT_Database_sorted.xlsx')
df = pd.DataFrame(df)
class_6 = df[df['class']==6]
topics = ['Knowing Our Numbers','Playing with Numbers','Whole Numbers', 'Negative Numbers and Integers', 'Fractions','Algebra','Ratio and Proportion', 'Geometry: Basic Geometrical Ideas', 'Understanding Elementary Shapes'
, 'Symmetry', 'Constructions', 'Mensuration: Concept of Perimeter and Introduction to Area', 'Data Handling']

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
