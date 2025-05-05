import streamlit as st
import pandas as pd
from topic_classifier import classify_prompt as classify_prompt  # For Aptitude Helper
from topic_classifier_class6_science import classify_prompt as science_classify_prompt_6
from topic_classifier_class6_maths import classify_prompt as maths_classify_prompt_6
from topic_classifier_class7_science import classify_prompt as science_classify_prompt_7
from topic_classifier_class7_maths import classify_prompt as maths_classify_prompt_7
from topic_classifier_class8_science import classify_prompt as science_classify_prompt_8
from topic_classifier_class8_maths import classify_prompt as maths_classify_prompt_8

# --- Set page config ---
st.set_page_config(
    page_title="ExamBuddy",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📚"
)

# --- Custom CSS for styling ---
st.markdown("""
    <style>
    .main { background-color: #f5f7fa; padding: 20px; }
    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        border: 2px solid #007bff;
    }
    .stButton > button {
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    .video-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    .video-card:hover {
        transform: translateY(-5px);
    }
    .topic-chip {
        background-color: #e9f5ff;
        color: #007bff;
        padding: 5px 10px;
        border-radius: 15px;
        margin-right: 5px;
        font-size: 14px;
        display: inline-block;
    }
    .filter-container {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stMultiSelect > div > div > div {
        border-radius: 10px;
        border: 2px solid #007bff;
        padding: 10px;
        font-size: 16px;
    }
    .stMultiSelect > div > div > div:hover {
        border-color: #0056b3;
    }
    h1 { color: #2c3e50; font-family: 'Arial', sans-serif; }
    h2 { color: #34495e; }
    h3 { color: #34495e; }
    .stVideo { max-width: 100%; margin: 0; padding: 0; }
    .section-divider { border-top: 2px solid #dcdcdc; margin: 30px 0; }
    .stSpinner { text-align: center; }
    .stTabs [data-baseweb="tab"] { font-size: 16px; font-weight: bold; }
    .stTabs [data-baseweb="tab"]:hover { background-color: #e9f5ff; }
    </style>
""", unsafe_allow_html=True)

# --- Load video dataset for Aptitude ---
@st.cache_data
def load_video_data():
    try:
        return pd.read_csv("data/final_video_details_logical.csv")
    except Exception as e:
        st.error(f"Error loading aptitude video data: {str(e)}")
        return pd.DataFrame()

def load_class6_data():
    try:
        df = pd.read_excel("data/DAV_YT_Database_sorted.xlsx")  # Replace with actual Class 8 dataset path
        df = pd.DataFrame(df)
        df = df[df['class']==6]
        if 'topic' in df.columns:
            df['topic'] = df['topic'].fillna('Unknown').astype(str)
        else:
            st.warning("The 'topic' column is missing in the Class 7 dataset. Using default 'Unknown' topic.")
            df['topic'] = 'Unknown'
        if 'subject' in df.columns:
            df['subject'] = df['subject'].fillna('Unknown').astype(str)
            df['subject'] = df['subject'].apply(lambda x: x if x in ['Science', 'Maths'] else 'Unknown')
        else:
            st.warning("The 'subject' column is missing in the Class 7 dataset. Using default 'Unknown' subject.")
            df['subject'] = 'Unknown'
        return df
    except Exception as e:
        st.error(f"Error loading Class 7 data: {str(e)}")
        return pd.DataFrame()


# --- Load Class 7 dataset ---
@st.cache_data
def load_class7_data():
    try:
        df = pd.read_excel("data/DAV_YT_Database_sorted.xlsx")  # Replace with actual Class 8 dataset path
        df = pd.DataFrame(df)
        df = df[df['class']==7]
        
        if 'topic' in df.columns:
            df['topic'] = df['topic'].fillna('Unknown').astype(str)
        else:
            st.warning("The 'topic' column is missing in the Class 7 dataset. Using default 'Unknown' topic.")
            df['topic'] = 'Unknown'
        if 'subject' in df.columns:
            df['subject'] = df['subject'].fillna('Unknown').astype(str)
            df['subject'] = df['subject'].apply(lambda x: x if x in ['Science', 'Maths'] else 'Unknown')
        else:
            st.warning("The 'subject' column is missing in the Class 7 dataset. Using default 'Unknown' subject.")
            df['subject'] = 'Unknown'
        return df
    except Exception as e:
        st.error(f"Error loading Class 7 data: {str(e)}")
        return pd.DataFrame()

# --- Load Class 8 dataset ---
@st.cache_data
def load_class8_data():
    try:
        df = pd.read_excel("data/DAV_YT_Database_sorted.xlsx")  # Replace with actual Class 8 dataset path
        df = pd.DataFrame(df)
        df = df[df['class']==8]
        if 'topic' in df.columns:
            df['topic'] = df['topic'].fillna('Unknown').astype(str)
        else:
            st.warning("The 'topic' column is missing in the Class 8 dataset. Using default 'Unknown' topic.")
            df['topic'] = 'Unknown'
        if 'subject' in df.columns:
            df['subject'] = df['subject'].fillna('Unknown').astype(str)
            df['subject'] = df['subject'].apply(lambda x: x if x in ['Science', 'Maths'] else 'Unknown')
        else:
            st.warning("The 'subject' column is missing in the Class 8 dataset. Using default 'Unknown' subject.")
            df['subject'] = 'Unknown'
        return df
    except Exception as e:
        st.error(f"Error loading Class 8 data: {str(e)}")
        return pd.DataFrame()

data = load_video_data()

class7_data = load_class7_data()
class8_data = load_class8_data()
class6_data = load_class6_data()

# --- Sidebar ---
with st.sidebar:
    st.image("https://via.placeholder.com/100", caption="ExamBuddy")  # Replace with your logo
    st.markdown("### Navigation")
    st.markdown("Choose a section to explore resources.")
    section = st.radio("Select Section", ["Aptitude Helper", "Class 6 Resources", "Class 7 Resources", "Class 8 Resources"])
    st.markdown("---")
    st.markdown("Made by KG")

# --- Main Content ---
st.title("📚 ExamBuddy")
st.markdown("Your companion for aptitude and school learning resources.")

# --- Aptitude Helper Section ---
if section == "Aptitude Helper":
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    st.header("🧠 Aptitude Helper")
    st.markdown("Master logical and quantitative aptitude with curated video resources.")

    with st.container():
        selected_aptitude_topics = st.multiselect(
            "Select Aptitude Topics",
            options=sorted([topic for topic in data['topic'].unique() if topic != 'Unknown']) if not data.empty else [],
            default=[],
            key="aptitude_topic_filter",
            placeholder="Choose topics to filter videos"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with st.container():
        query = st.text_input(
            "🔍 Search for a topic or question:",
            placeholder="E.g., Probability, Logical Reasoning",
            key="aptitude_search"
        )
        search_button = st.button("Search", key="aptitude_search_button", use_container_width=True)

    if query and search_button:
        with st.spinner("Finding the best videos for you..."):
            predicted_topics = classify_prompt(query, top_k=2)
            if predicted_topics:
                st.markdown("**Matched Topics:** " + " ".join(
                    [f"<span class='topic-chip'>{topic}</span>" for topic in predicted_topics]
                ), unsafe_allow_html=True)
                filtered_videos = data[data['topic'].isin(predicted_topics)]
                if selected_aptitude_topics:
                    filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_aptitude_topics)]
                filtered_videos = filtered_videos.copy()
                filtered_videos['topic'] = pd.Categorical(
                    filtered_videos['topic'],
                    categories=predicted_topics,
                    ordered=True
                )
                filtered_videos = filtered_videos.sort_values(by='topic')
                if not filtered_videos.empty:
                    st.markdown("### Recommended Videos")
                    filtered_videos = filtered_videos.head(15)
                    for idx, row in filtered_videos.iterrows():
                        with st.container():
                            if row['link']:
                                try:
                                    st.video(row['link'])
                                    st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                                except Exception as e:
                                    st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                            else:
                                st.warning(f"Invalid or missing URL for video: {row['title']}")
                            st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.warning("No videos found for the selected topics.")
            else:
                st.error("Couldn’t classify the query into known topics.")
    else:
        st.markdown("### Explore Aptitude Videos")
        filtered_videos = data
        if selected_aptitude_topics:
            filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_aptitude_topics)]
        if not filtered_videos.empty:
            filtered_videos = filtered_videos.head(15)
            for idx, row in filtered_videos.iterrows():
                with st.container():
                    if row['link']:
                        try:
                            st.video(row['link'])
                            st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                        except Exception as e:
                            st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                    else:
                        st.warning(f"Invalid or missing URL for video: {row['title']}")
                    st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("No videos match the selected filters.")

# --- Class 6 Resources Section ---
elif section == "Class 6 Resources":
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    st.header("📚 Class 6 Learning Resources")
    st.markdown("Explore curated video resources for Class 6 Science and Maths topics.")

    science_tab, maths_tab = st.tabs(["🔬 Science", "➕ Maths"])

    with science_tab:
        st.session_state['class6_tab'] = "Science"
        with st.container():
            selected_science_topics = st.multiselect(
                "Select Science Topics",
                options=['Food', 'Materials', 'The World of The Living', 'Moving Things, People and Ideas', 'How Things Work', 'Natural Phenomena', 'Natural Resources', 'Electric current and circuits', 'Magnets', 'Rain, thunder and lightning', 'Light', 'Importance of air', 'Waste'],
                default=[],
                key="science_topic_filter_6",
                placeholder="Choose topics to filter videos"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with st.container():
            query_science = st.text_input(
                "🔍 Search for a Science topic or question:",
                placeholder="E.g., Photosynthesis, Force",
                key="science_search_6"
            )
            search_button_science = st.button("Search Science", key="science_search_button_6", use_container_width=True)

        if query_science and search_button_science:
            with st.spinner("Finding the best Science videos for you..."):
                predicted_topics = science_classify_prompt_6(query_science, top_k=2)
                if predicted_topics:
                    st.markdown("**Matched Science Topics:** " + " ".join(
                        [f"<span class='topic-chip'>{topic}</span>" for topic in predicted_topics]
                    ), unsafe_allow_html=True)
                    filtered_videos = class6_data[(class6_data['subject'] == 'Science') & (class6_data['topic'].isin(predicted_topics))]
                    if selected_science_topics:
                        filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_science_topics)]
                    filtered_videos = filtered_videos.copy()
                    filtered_videos['topic'] = pd.Categorical(
                        filtered_videos['topic'],
                        categories=predicted_topics,
                        ordered=True
                    )
                    filtered_videos = filtered_videos.sort_values(by='topic')
                    if not filtered_videos.empty:
                        st.markdown("### Recommended Science Videos")
                        filtered_videos = filtered_videos.head(15)
                        for idx, row in filtered_videos.iterrows():
                            with st.container():
                                if row['link']:
                                    try:
                                        st.video(row['link'])
                                        st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                                    except Exception as e:
                                        st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                                else:
                                    st.warning(f"Invalid or missing URL for video: {row['title']}")
                                st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.warning("No Science videos found for the selected topics.")
                else:
                    st.error("Couldn’t classify the Science query into known topics.")
        else:
            st.markdown("### Explore Science Videos")
            filtered_videos = class6_data[class6_data['subject'] == 'Science']
            if selected_science_topics:
                filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_science_topics)]
            if not filtered_videos.empty:
                filtered_videos = filtered_videos.head(15)
                for idx, row in filtered_videos.iterrows():
                    with st.container():
                        if row['link']:
                            try:
                                st.video(row['link'])
                                st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                            except Exception as e:
                                st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                        else:
                            st.warning(f"Invalid or missing URL for video: {row['title']}")
                        st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("No Science videos available.")

    with maths_tab:
        st.session_state['class6_tab'] = "Maths"
        with st.container():
            selected_maths_topics = st.multiselect(
                "Select Maths Topics",
                options=['Knowing Our Numbers', 'Playing with Numbers', 'Whole Numbers', 'Negative Numbers and Integers', 'Fractions', 'Algebra', 'Ratio and Proportion', 'Geometry: Basic Geometrical Ideas', 'Understanding Elementary Shapes', 'Symmetry', 'Constructions', 'Mensuration: Concept of Perimeter and Introduction to Area', 'Data Handling'],
                default=[],
                key="maths_topic_filter_6",
                placeholder="Choose topics to filter videos"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with st.container():
            query_maths = st.text_input(
                "🔍 Search for a Maths topic or question:",
                placeholder="E.g., Fractions, Algebra",
                key="maths_search_6"
            )
            search_button_maths = st.button("Search Maths", key="maths_search_button_6", use_container_width=True)

        if query_maths and search_button_maths:
            with st.spinner("Finding the best Maths videos for you..."):
                predicted_topics = maths_classify_prompt_6(query_maths, top_k=2)
                if predicted_topics:
                    st.markdown("**Matched Maths Topics:** " + " ".join(
                        [f"<span class='topic-chip'>{topic}</span>" for topic in predicted_topics]
                    ), unsafe_allow_html=True)
                    filtered_videos = class6_data[(class6_data['subject'] == 'Maths') & (class6_data['topic'].isin(predicted_topics))]
                    if selected_maths_topics:
                        filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_maths_topics)]
                    filtered_videos = filtered_videos.copy()
                    filtered_videos['topic'] = pd.Categorical(
                        filtered_videos['topic'],
                        categories=predicted_topics,
                        ordered=True
                    )
                    filtered_videos = filtered_videos.sort_values(by='topic')
                    if not filtered_videos.empty:
                        st.markdown("### Recommended Maths Videos")
                        filtered_videos = filtered_videos.head(15)
                        for idx, row in filtered_videos.iterrows():
                            with st.container():
                                if row['link']:
                                    try:
                                        st.video(row['link'])
                                        st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                                    except Exception as e:
                                        st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                                else:
                                    st.warning(f"Invalid or missing URL for video: {row['title']}")
                                st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.warning("No Maths videos found for the selected topics.")
                else:
                    st.error("Couldn’t classify the Maths query into known topics.")
        else:
            st.markdown("### Explore Maths Videos")
            filtered_videos = class6_data[class6_data['subject'] == 'Maths']
            if selected_maths_topics:
                filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_maths_topics)]
            if not filtered_videos.empty:
                filtered_videos = filtered_videos.head(15)
                for idx, row in filtered_videos.iterrows():
                    with st.container():
                        if row['link']:
                            try:
                                st.video(row['link'])
                                st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                            except Exception as e:
                                st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                        else:
                            st.warning(f"Invalid or missing URL for video: {row['title']}")
                        st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("No Maths videos available.")

# --- Class 7 Resources Section ---
elif section == "Class 7 Resources":
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    st.header("📚 Class 7 Learning Resources")
    st.markdown("Explore curated video resources for Class 7 Science and Maths topics.")

    science_tab, maths_tab = st.tabs(["🔬 Science", "➕ Maths"])

    with science_tab:
        st.session_state['class7_tab'] = "Science"
        with st.container():
            selected_science_topics = st.multiselect(
                "Select Science Topics",
                options=[
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
],
                default=[],
                key="science_topic_filter_7",
                placeholder="Choose topics to filter videos"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with st.container():
            query_science = st.text_input(
                "🔍 Search for a Science topic or question:",
                placeholder="E.g., Respiration, Light",
                key="science_search_7"
            )
            search_button_science = st.button("Search Science", key="science_search_button_7", use_container_width=True)

        if query_science and search_button_science:
            with st.spinner("Finding the best Science videos for you..."):
                predicted_topics = science_classify_prompt_7(query_science, top_k=2)
                if predicted_topics:
                    st.markdown("**Matched Science Topics:** " + " ".join(
                        [f"<span class='topic-chip'>{topic}</span>" for topic in predicted_topics]
                    ), unsafe_allow_html=True)
                    filtered_videos = class7_data[(class7_data['subject'] == 'Science') & (class7_data['topic'].isin(predicted_topics))]
                    if selected_science_topics:
                        filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_science_topics)]
                    filtered_videos = filtered_videos.copy()
                    filtered_videos['topic'] = pd.Categorical(
                        filtered_videos['topic'],
                        categories=predicted_topics,
                        ordered=True
                    )
                    filtered_videos = filtered_videos.sort_values(by='topic')
                    if not filtered_videos.empty:
                        st.markdown("### Recommended Science Videos")
                        filtered_videos = filtered_videos.head(15)
                        for idx, row in filtered_videos.iterrows():
                            with st.container():
                                if row['link']:
                                    try:
                                        st.video(row['link'])
                                        st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                                    except Exception as e:
                                        st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                                else:
                                    st.warning(f"Invalid or missing URL for video: {row['title']}")
                                st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.warning("No Science videos found for the selected topics.")
                else:
                    st.error("Couldn’t classify the Science query into known topics.")
        else:
            st.markdown("### Explore Science Videos")
            filtered_videos = class7_data[class7_data['subject'] == 'Science']
            if selected_science_topics:
                filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_science_topics)]
            if not filtered_videos.empty:
                filtered_videos = filtered_videos.head(15)
                for idx, row in filtered_videos.iterrows():
                    with st.container():
                        if row['link']:
                            try:
                                st.video(row['link'])
                                st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                            except Exception as e:
                                st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                        else:
                            st.warning(f"Invalid or missing URL for video: {row['title']}")
                        st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("No Science videos available.")

    with maths_tab:
        st.session_state['class7_tab'] = "Maths"
        with st.container():
            selected_maths_topics = st.multiselect(
                "Select Maths Topics",
                options=[
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
],
                default=[],
                key="maths_topic_filter_7",
                placeholder="Choose topics to filter videos"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with st.container():
            query_maths = st.text_input(
                "🔍 Search for a Maths topic or question:",
                placeholder="E.g., Rational Numbers, Geometry",
                key="maths_search_7"
            )
            search_button_maths = st.button("Search Maths", key="maths_search_button_7", use_container_width=True)

        if query_maths and search_button_maths:
            with st.spinner("Finding the best Maths videos for you..."):
                predicted_topics = maths_classify_prompt_7(query_maths, top_k=2)
                if predicted_topics:
                    st.markdown("**Matched Maths Topics:** " + " ".join(
                        [f"<span class='topic-chip'>{topic}</span>" for topic in predicted_topics]
                    ),unsafe_allow_html=True)
                    filtered_videos = class7_data[(class7_data['subject'] == 'Maths') & (class7_data['topic'].isin(predicted_topics))]
                    if selected_maths_topics:
                        filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_maths_topics)]
                    filtered_videos = filtered_videos.copy()
                    filtered_videos['topic'] = pd.Categorical(
                        filtered_videos['topic'],
                        categories=predicted_topics,
                        ordered=True
                    )
                    filtered_videos = filtered_videos.sort_values(by='topic')
                    if not filtered_videos.empty:
                        st.markdown("### Recommended Maths Videos")
                        filtered_videos = filtered_videos.head(15)
                        for idx, row in filtered_videos.iterrows():
                            with st.container():
                                if row['link']:
                                    try:
                                        st.video(row['link'])
                                        st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                                    except Exception as e:
                                        st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                                else:
                                    st.warning(f"Invalid or missing URL for video: {row['title']}")
                                st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.warning("No Maths videos found for the selected topics.")
                else:
                    st.error("Couldn’t classify the Maths query into known topics.")
        else:
            st.markdown("### Explore Maths Videos")
            filtered_videos = class7_data[class7_data['subject'] == 'Maths']
            if selected_maths_topics:
                filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_maths_topics)]
            if not filtered_videos.empty:
                filtered_videos = filtered_videos.head(15)
                for idx, row in filtered_videos.iterrows():
                    with st.container():
                        if row['link']:
                            try:
                                st.video(row['link'])
                                st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                            except Exception as e:
                                st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                        else:
                            st.warning(f"Invalid or missing URL for video: {row['title']}")
                        st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("No Maths videos available.")

# --- Class 8 Resources Section ---
elif section == "Class 8 Resources":
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    st.header("📚 Class 8 Learning Resources")
    st.markdown("Explore curated video resources for Class 8 Science and Maths topics.")

    science_tab, maths_tab = st.tabs(["🔬 Science", "➕ Maths"])

    with science_tab:
        st.session_state['class8_tab'] = "Science"
        with st.container():
            selected_science_topics = st.multiselect(
                "Select Science Topics",
                options= [
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
],
                default=[],
                key="science_topic_filter_8",
                placeholder="Choose topics to filter videos"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with st.container():
            query_science = st.text_input(
                "🔍 Search for a Science topic or question:",
                placeholder="E.g., Friction, Cell Structure",
                key="science_search_8"
            )
            search_button_science = st.button("Search Science", key="science_search_button_8", use_container_width=True)

        if query_science and search_button_science:
            with st.spinner("Finding the best Science videos for you..."):
                predicted_topics = science_classify_prompt_8(query_science, top_k=2)
                if predicted_topics:
                    st.markdown("**Matched Science Topics:** " + " ".join(
                        [f"<span class='topic-chip'>{topic}</span>" for topic in predicted_topics]
                    ), unsafe_allow_html=True)
                    filtered_videos = class8_data[(class8_data['subject'] == 'Science') & (class8_data['topic'].isin(predicted_topics))]
                    if selected_science_topics:
                        filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_science_topics)]
                    filtered_videos = filtered_videos.copy()
                    filtered_videos['topic'] = pd.Categorical(
                        filtered_videos['topic'],
                        categories=predicted_topics,
                        ordered=True
                    )
                    filtered_videos = filtered_videos.sort_values(by='topic')
                    if not filtered_videos.empty:
                        st.markdown("### Recommended Science Videos")
                        filtered_videos = filtered_videos.head(15)
                        for idx, row in filtered_videos.iterrows():
                            with st.container():
                                if row['link']:
                                    try:
                                        st.video(row['link'])
                                        st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                                    except Exception as e:
                                        st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                                else:
                                    st.warning(f"Invalid or missing URL for video: {row['title']}")
                                st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.warning("No Science videos found for the selected topics.")
                else:
                    st.error("Couldn’t classify the Science query into known topics.")
        else:
            st.markdown("### Explore Science Videos")
            filtered_videos = class8_data[class8_data['subject'] == 'Science']
            if selected_science_topics:
                filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_science_topics)]
            if not filtered_videos.empty:
                filtered_videos = filtered_videos.head(15)
                for idx, row in filtered_videos.iterrows():
                    with st.container():
                        if row['link']:
                            try:
                                st.video(row['link'])
                                st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                            except Exception as e:
                                st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                        else:
                            st.warning(f"Invalid or missing URL for video: {row['title']}")
                        st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("No Science videos available.")

    with maths_tab:
        st.session_state['class8_tab'] = "Maths"
        with st.container():
            selected_maths_topics = st.multiselect(
                "Select Maths Topics",
                options=[
    "Rational Numbers",
    "Linear Equations in One Variable",
    "Understanding Quadrilaterals",
    "Data Handling",
    "Squares and Square Roots",
    "Cubes and Cube Roots",
    "Comparing Quantities",
    "Algebraic Expressions and Identities",
    "Mensuration",
    "Exponents and Powers",
    "Direct and Inverse Proportions",
    "Factorisation",
    "Introduction to Graphs"
],
                default=[],
                key="maths_topic_filter_8",
                placeholder="Choose topics to filter videos"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with st.container():
            query_maths = st.text_input(
                "🔍 Search for a Maths topic or question:",
                placeholder="E.g., Linear Equations, Mensuration",
                key="maths_search_8"
            )
            search_button_maths = st.button("Search Maths", key="maths_search_button_8", use_container_width=True)

        if query_maths and search_button_maths:
            with st.spinner("Finding the best Maths videos for you..."):
                predicted_topics = maths_classify_prompt_8(query_maths, top_k=2)
                if predicted_topics:
                    st.markdown("**Matched Maths Topics:** " + " ".join(
                        [f"<span class='topic-chip'>{topic}</span>" for topic in predicted_topics]
                    ), unsafe_allow_html=True)
                    filtered_videos = class8_data[(class8_data['subject'] == 'Maths') & (class8_data['topic'].isin(predicted_topics))]
                    if selected_maths_topics:
                        filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_maths_topics)]
                    filtered_videos = filtered_videos.copy()
                    filtered_videos['topic'] = pd.Categorical(
                        filtered_videos['topic'],
                        categories=predicted_topics,
                        ordered=True
                    )
                    filtered_videos = filtered_videos.sort_values(by='topic')
                    if not filtered_videos.empty:
                        st.markdown("### Recommended Maths Videos")
                        filtered_videos = filtered_videos.head(15)
                        for idx, row in filtered_videos.iterrows():
                            with st.container():
                                if row['link']:
                                    try:
                                        st.video(row['link'])
                                        st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                                    except Exception as e:
                                        st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                                else:
                                    st.warning(f"Invalid or missing URL for video: {row['title']}")
                                st.markdown("</div>", unsafe_allow_html=True)
                    else:
                        st.warning("No Maths videos found for the selected topics.")
                else:
                    st.error("Couldn’t classify the Maths query into known topics.")
        else:
            st.markdown("### Explore Maths Videos")
            filtered_videos = class8_data[class8_data['subject'] == 'Maths']
            if selected_maths_topics:
                filtered_videos = filtered_videos[filtered_videos['topic'].isin(selected_maths_topics)]
            if not filtered_videos.empty:
                filtered_videos = filtered_videos.head(15)
                for idx, row in filtered_videos.iterrows():
                    with st.container():
                        if row['link']:
                            try:
                                st.video(row['link'])
                                st.markdown(f"**{row['title']}** (Topic: {row['topic']})")
                            except Exception as e:
                                st.warning(f"Failed to load video: {row['title']} ({row['link']}). Error: {str(e)}")
                        else:
                            st.warning(f"Invalid or missing URL for video: {row['title']}")
                        st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("No Maths videos available.")