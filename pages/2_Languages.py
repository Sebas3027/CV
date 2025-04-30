import streamlit as st
import pandas as pd
import altair as alt

# Page config and styling
st.set_page_config(page_title="Languages", layout="wide")

st.markdown("""
    <style>
        .stApp {
            background-image: url("https://www.transparenttextures.com/patterns/cubes.png");
            background-size: cover;
        }
        .lang-section {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 10px;
        }
        .lang-story {
            font-size: 17px;
            margin-bottom: 1.5rem;
        }
        h2 {
            margin-top: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center;'> Language Proficiency</h1>", unsafe_allow_html=True)

# Language Data & Chart
langs = pd.DataFrame({
    "Language": ["Dutch", "English", "German"],
    "Proficiency (%)": [100, 90, 70]
})

chart = alt.Chart(langs).mark_arc(innerRadius=50).encode(
    theta="Proficiency (%):Q",
    color="Language:N",
    tooltip=["Language", "Proficiency (%)"]
).properties(height=300)

col1, col2 = st.columns([1, 2])
with col1:
    st.altair_chart(chart, use_container_width=True)

with col2:
    st.markdown("<div class='lang-section'>", unsafe_allow_html=True)
    
    st.markdown("""
    ### 🇳🇱 Dutch
    <div class='lang-story'>
    I was born and raised in the Netherlands, so Dutch is my native language. It's the language I grew up speaking every day.
    </div>
    
    ### 🇬🇧 English
    <div class='lang-story'>
    I've used English throughout my life, both in daily communication and in education. My entire Bachelor's degree was taught in English, so I'm very comfortable with academic and technical English as well.
    </div>
    
    ### 🇩🇪 German
    <div class='lang-story'>
    I studied German in middle school and I live near the German border. While I'm not fluent, I can easily make myself understood in everyday situations.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("📇 Contact")
st.sidebar.write("📍 6351EK, Bocholtz")
st.sidebar.write("📞 +31 0623042382")
st.sidebar.write("✉️ sebasvansluijsdam@gmail.com")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/sebas-van-sluijsdam-2704svs/)")
