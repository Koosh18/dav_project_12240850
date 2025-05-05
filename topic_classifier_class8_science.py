from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
df = pd.read_excel('data/DAV_YT_Database_sorted.xlsx')
df = pd.DataFrame(df)
class_6 = df[df['class']==6]
topics = [
    "Crop Production and Management",
    "Microorganisms: Friend and Foe",
    "Coal and Petroleum",
    "Combustion and Flame",
    "Conservation of Plants and Animals",
    "Reproduction in Animals",
    "Reaching the Age of Adolescence",
    "Force and Pressure",
    "Friction",
    "Sound",
    "Chemical Effects of Electric Current",
    "Some Natural Phenomena",
    "Light"
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
