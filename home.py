import streamlit as st

# Page config with a wider layout
st.set_page_config(page_title="Sebas van Sluijsdam - Home", layout="wide")

# Custom CSS for background and styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            padding: 2rem;
        }
        h1 {
            color: #2c3e50;
        }
        .stApp {
            background-image: url('https://www.transparenttextures.com/patterns/cubes.png');
            background-size: cover;
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.title("Interactive CV Sebas van Sluijsdam")

# Welcome message
st.markdown("""
Hi there! I'm **Sebas van Sluijsdam**, a master's student in Computer Science with a background in Data Science & AI.  
Welcome to my interactive CV! This site lets you explore my skills, experience, education, and more — in a dynamic and data-driven way.

Use the menu on the left to navigate.
""")

# Optional: Profile picture
col1, col2 = st.columns([1, 3])
with col1:
    st.image("IMG20250124115819~4.jpg", width=180)  # Adjust path or use another image
with col2:
    st.markdown("""
    #### 📍 Location  
    Bocholtz, Netherlands — currently studying in Aachen

    #### 📬 Contact  
    - 📧 [sebasvansluijsdam@gmail.com](mailto:sebasvansluijsdam@gmail.com) 
    - 📞 +31 0623042382
    - 💼 [LinkedIn](https://www.linkedin.com/in/sebas-van-sluijsdam-2704svs/)
    """)


