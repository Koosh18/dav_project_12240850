from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 📌 Topics to match against
topics = [
    # Logical Reasoning (1-30)
    "Alphanumeric series", "Reasoning Analogies", "Artificial Language", "Blood Relations", "Calendars",
    "Cause and Effect", "Clocks", "Coding-Decoding", "Critical path", "Cubes and cuboids",
    "Data Sufficiency", "Decision Making", "Deductive Reasoning/Statement Analysis", "Dices", "Directions",
    "Embedded Images", "Figure Matrix", "Input-Output", "Mirror and Water Images", "Odd One Out",
    "Picture Series and Sequences", "Paper Folding", "Puzzles", "Pattern Series and Sequences", "Order & Ranking",
    "Seating Arrangements", "Shape Construction", "Statement and Assumptions", "Statement and Conclusions", "Syllogism",

    # Quantitative Aptitude (31-72)
    "Algebra", "Alligations and mixtures", "Area", "Problems on Age", "Averages, Mean, Median and Mode",
    "Boat Problems", "Chain rule", "Discount", "Data Interpretation", "Games and Races",
    "Heights and distances", "Inequalities", "Number Series", "LCM and HCF", "Linear Equations",
    "Logarithms", "Number theory", "Number System – Fractions, Decimals", "Partnerships", "Percentage",
    "Permutation and Combinations", "Pipes and Cisterns", "Points, lines and angles", "Probability",
    "Profit and Loss", "Progressions", "Quadratic Equations", "Ratio and Proportions", "Remainder theorem and unit digit",
    "Sets and Venn Diagrams", "Simple and Compound Interest", "Simplification and Approximation",
    "Speed, Distance and Time", "Stocks and shares", "Data Sufficiency", "Surds, Indices, Exponents, and Powers",
    "Surface area", "Time and Work", "Problems on Train", "Trigonometry", "Volumes", "Work and Wages"
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
