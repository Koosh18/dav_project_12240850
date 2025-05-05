from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
df = pd.read_excel('data/DAV_YT_Database_sorted.xlsx')
df = pd.DataFrame(df)
class_6 = df[df['class']==6]
topics = [
 " Nutrition in Animals",
 "Fibre to Fabric",
 "Heat",
"Acids, Bases and Salts",
"Physical and Chemical Changes",
"Weather, Climate and Adaptations of Animals of Climate",
"Winds, Storms and Cyclones",
"Soil",
"Respiration in Organisms",
"Transportation in Animals and Plants",
"Reproduction in Plants",
"Motion and Time",
"Electric Current and its Effects",
"Light",
"Water: A Precious Resource",
"Forests: Our Lifeline",
 "Wastewater Story"
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
