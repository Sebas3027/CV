import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import date

# Page config and style
st.set_page_config(page_title="Education", layout="wide")

st.markdown("""
    <style>
        .stApp {
            background-image: url("https://www.transparenttextures.com/patterns/lined-paper.png");
            background-size: cover;
        }
        .edu-block {
            background-color: rgba(255, 255, 255, 0.92);
            padding: 1.5rem;
            margin-bottom: 2rem;
            border-radius: 10px;
            box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
        }
        .edu-title {
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 0.2rem;
        }
        .edu-dates {
            font-style: italic;
            color: #666;
            margin-bottom: 1rem;
        }
        .edu-description {
            font-size: 17px;
            line-height: 1.5;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'> Education</h1>", unsafe_allow_html=True)

# --- Education Blocks ---
with st.container():
    st.markdown("""
    <div class='edu-block'>
        <div class='edu-title'>MSc Computer Science – RWTH Aachen</div>
        <div class='edu-dates'>2025 – Present</div>
        <div class='edu-description'>
            Currently pursuing a Master's in Computer Science where I want to focus on:
            <ul>
                <li>Artificial Intelligence & Machine Learning</li>
                <li>Data Science</li>
                <li>Embedded Systems & Real-Time Computing</li>
            </ul>
            I’m deepening my knowledge in areas such as data science, machine learning, and embedded systems.  
            This program allows me to explore how intelligent algorithms can interact with real-world hardware and systems.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='edu-block'>
        <div class='edu-title'>BSc Data Science & AI – Maastricht University</div>
        <div class='edu-dates'>2020 – 2024</div>
        <div class='edu-description'>
           Built a strong foundation in artificial intelligence, statistics, and machine learning through Maastricht University's Problem-Based Learning (PBL) approach.  
            This method emphasized critical thinking, teamwork, and self-directed learning in small groups.  
            Gained hands-on experience with Python, scikit-learn, and real-world data through projects and assignments.  
            <br><br>
            <strong>Key courses:</strong> Machine Learning, AI, Probability, Programming in Python/Java, Neural Networks, Data Ethics.  
            <strong>Skills gained:</strong> ML model development, team collaboration, scientific writing.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='edu-block'>
        <div class='edu-title'>VWO (NT + NG + Informatica) – Bernardinus College</div>
        <div class='edu-dates'>2014 – 2020</div>
        <div class='edu-description'>
            Dual-profile VWO in Nature & Technology and Nature & Health with electives in Informatica.  
            My profile paper (profielwerkstuk) focused on game design in Python, sparking my interest in algorithms and interactivity.  
            <br><br>
            <strong>Skills gained:</strong> early programming logic, scientific problem solving, time management, independent research.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.subheader("Grades by Course Category")

# Data: course, grade, is_project, category
data = [
    ("Intro to DS & AI", 7.0, False, "Foundations"),
    ("Intro to CS 1", 6.0, False, "Programming"),
    ("Discrete Math", 7.0, False, "Math"),
    ("Cognitive Neuroscience", 7.0, False, "AI & Cognition"),
    ("Intro to CS 2", 6.0, False, "Programming"),
    ("Project 1-1", 7.5, True, "Projects"),
    ("Linear Algebra", 8.0, False, "Math"),
    ("Data Structures & Algos", 9.0, False, "Programming"),
    ("ICT & Knowledge Mgmt", 8.0, False, "Systems"),
    ("Software Eng.", 7.0, False, "Programming"),
    ("Logic", 8.0, False, "Math"),
    ("Calculus", 8.0, False, "Math"),
    ("Numerical Math", 6.0, False, "Math"),
    ("Project 1-2", 6.0, True, "Projects"),
    ("Databases", 7.0, False, "Systems"),
    ("Philosophy & AI", 7.0, False, "AI & Cognition"),
    ("Probability & Stats", 6.0, False, "Math"),
    ("Graph Theory", 9.0, False, "Math"),
    ("Reasoning Techniques", 6.0, False, "Logic & Reasoning"),
    ("Project 2-1", 7.0, True, "Projects"),
    ("HCI & Affective Comp.", 7.0, False, "AI & Cognition"),
    ("Math Modelling", 6.0, False, "Math"),
    ("Linear Programming", 8.0, False, "Math"),
    ("Simulation & Stat. Analysis", 6.0, False, "Math"),
    ("Machine Learning", 8.0, False, "AI & ML"),
    ("NLP", 7.0, False, "AI & ML"),
    ("Project 2-2", 6.5, True, "Projects"),
    ("Image & Video Processing", 6.0, False, "AI & ML"),
    ("Game Theory", 7.0, False, "Logic & Reasoning"),
    ("Project 3-1", 6.0, True, "Projects"),
    ("Bioinformatics", 7.0, False, "AI & ML"),
    ("Semantic Web", 6.0, False, "Systems"),
    ("Computer Security", 6.0, False, "Systems"),
    ("Recommender Systems", 7.0, False, "AI & ML"),
    ("Operations Research", 8.0, False, "Math"),
    ("Intelligent Systems", 7.0, False, "AI & ML"),
    ("Data Analysis", 7.0, False, "AI & ML"),
    ("Bachelor Thesis", 7.0, True, "Projects")
]

df = pd.DataFrame(data, columns=["Course", "Grade", "Project", "Category"])
df["Course"] = df["Course"].str.wrap(25)  # Voor betere layout als je lange namen gebruikt

custom_order = [
    "Math", "Programming", "AI & ML", "AI & Cognition", "Projects",
    "Systems", "Logic & Reasoning", "Foundations"
]
categories = [cat for cat in custom_order if cat in df["Category"].unique()]


# Maak voor elke categorie een eigen bar chart
figs = []

for cat in categories:
    sub_df = df[df["Category"] == cat].sort_values("Grade", ascending=True)
    fig = px.bar(
        sub_df,
        x="Grade",
        y="Course",
        orientation="h",
        color="Project",
        title=f"{cat} Grades",
        color_discrete_map={True: "#1f77b4", False: "#1f77b4"},
        height=300
    )
    fig.update_layout(
        showlegend=False,
        xaxis=dict(range=[5.5, 10], title="Grade"),
        yaxis_title=None,
        margin=dict(t=40)
    )
    figs.append(fig)

# Verdeel in rijen van 2 grafieken
rows = [figs[i:i + 2] for i in range(0, len(figs), 2)]

for row in rows:
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(row[0], use_container_width=True)
    if len(row) > 1:
        with col2:
            st.plotly_chart(row[1], use_container_width=True)

# --- Sidebar ---
st.sidebar.header("📇 Contact")
st.sidebar.write("📍 6351EK, Bocholtz")
st.sidebar.write("📞 +31 0623042382")
st.sidebar.write("✉️ sebasvansluijsdam@gmail.com")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/sebas-van-sluijsdam-2704svs/)")
