import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# Page config and styling
st.set_page_config(page_title="Skills Overview", layout="wide")

st.markdown("""
    <style>
        .stApp {
            background-image: url("https://www.transparenttextures.com/patterns/cubes.png");
            background-size: cover;
        }
        .intro-text {
            background-color: rgba(255, 255, 255, 0.95);
            padding: 1.5rem;
            margin-bottom: 2rem;
            border-radius: 10px;
        }
        .block-section {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
        }
        .section-title {
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 0.8rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Intro
st.markdown("<div class='intro-text'>", unsafe_allow_html=True)
st.markdown("""
##  My Skills Overview  
Throughout my studies and work experience, I’ve developed a broad set of technical and soft skills — from hands-on programming and data analysis to clear communication and collaborative teamwork in fast-paced environments.
""")
st.markdown("</div>", unsafe_allow_html=True)

# --- Technical and Soft Skills Columns ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='block-section'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'> Technical Skills (Bar)</div>", unsafe_allow_html=True)

    st.markdown("These are core technical skills I've built through academic coursework, side projects, and real-world tasks — from programming to working with data and algorithms.")

    skills = pd.DataFrame({
        "Skill": ["Python", "Java", "SQL", "Machine learning", "Matlab", "C"],
        "Level": [90, 70, 65, 75, 80, 60]
    })
    chart = alt.Chart(skills).mark_bar().encode(
        x=alt.X("Level:Q", scale=alt.Scale(domain=[0, 100])),
        y=alt.Y("Skill:N", sort='-x'),
        color="Level:Q",
        tooltip=["Skill", "Level"]
    ).properties(height=350)
    st.altair_chart(chart, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='block-section'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'> Soft Skills</div>", unsafe_allow_html=True)

    st.markdown("Soft skills help me succeed in teams and projects — I value feedback, structure, and clear communication.")
    st.markdown("""
    -  Team collaboration  
    -  Communication (written & verbal)  
    -  Problem-solving  
    -  Critical thinking  
    -  Time management  
    -  Attention to detail  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Radar Chart Section ---
st.markdown("<div class='block-section'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'> Technical Skills (Radar View)</div>", unsafe_allow_html=True)

fig = px.line_polar(skills, r='Level', theta='Skill', line_close=True)
fig.update_traces(fill='toself')
fig.update_layout(height=450, margin=dict(t=20))
st.plotly_chart(fig)
st.markdown("</div>", unsafe_allow_html=True)

# --- Tools & Frameworks ---
st.markdown("<div class='block-section'>", unsafe_allow_html=True)
st.markdown("<div class='section-title'> Tools & Frameworks</div>", unsafe_allow_html=True)

st.markdown("""
I’m familiar with various tools that support coding, collaboration, and publishing:

-  Git & GitHub   
-  Jupyter Notebook  
-  VS Code & PyCharm  
-  Linux (basic usage)  
-  LaTeX
""")
st.markdown("</div>", unsafe_allow_html=True)

# --- Sidebar Contact ---
st.sidebar.header("📇 Contact")
st.sidebar.write("📍 6351EK, Bocholtz")
st.sidebar.write("📞 +31 0623042382")
st.sidebar.write("✉️ sebasvansluijsdam@gmail.com")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/sebas-van-sluijsdam-2704svs/)")
