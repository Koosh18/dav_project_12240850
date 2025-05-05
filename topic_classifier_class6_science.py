from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
df = pd.read_excel('data/DAV_YT_Database_sorted.xlsx')
df = pd.DataFrame(df)
class_6 = df[df['class']==6]
topics = ['Food','Materials', 'The World of The Living', 'Moving Things, People and Ideas', 'How Things Work', 'Natural Phenomena', 'Natural Resources', 'Electric current and circuits','Magnets', 'Rain, thunder and lightning','Light','Importance of air','Waste']

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
