import streamlit as st

# Page config and style
st.set_page_config(page_title="Work Experience", layout="wide")

st.markdown("""
    <style>
        .stApp {
            background-image: url("https://www.transparenttextures.com/patterns/circles.png");
            background-size: cover;
        }
        .experience-block {
            background-color: rgba(255, 255, 255, 0.92);
            padding: 1.5rem;
            margin-bottom: 2rem;
            border-radius: 10px;
            box-shadow: 1px 1px 5px rgba(0,0,0,0.1);
        }
        .job-title {
            font-size: 22px;
            font-weight: 600;
        }
        .job-dates {
            font-style: italic;
            color: #666;
            margin-bottom: 1rem;
        }
        .job-summary {
            font-size: 17px;
            line-height: 1.5;
        }
        ul.skills {
            padding-left: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Work Experience</h1>", unsafe_allow_html=True)

# Experience Entries
with st.container():
    st.markdown("""
    <div class='experience-block'>
        <div class='job-title'>Algebrakit (Lead Author)</div>
        <div class='job-dates'>Nov 2022 – Present</div>
        <div class='job-summary'>
            I together with two other people led a small team of authors and collaborated with developers and clients to shape interactive math content for an educational platform.  
            My responsibilities included reviewing and guiding the work of junior authors, providing feedback, testing new product features, and communicating directly with clients to align content with their needs.
            <br><br>
            <strong>Skills developed:</strong>
            <ul class='skills'>
                <li>Leadership & mentoring</li>
                <li>Client communication</li>
                <li>Analytical thinking</li>
                <li>Educational content creation</li>
                <li>Attention to detail</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='experience-block'>
        <div class='job-title'>Wismon (Content Editor)</div>
        <div class='job-dates'>Apr 2022 – Nov 2022</div>
        <div class='job-summary'>
            At Wismon, I created and edited STEM learning materials for Dutch high school curricula.  
            I worked closely with subject-matter experts and used CMS tools to produce educational content.
            <br><br>
            <strong>Skills developed:</strong>
            <ul class='skills'>
                <li>Science communication</li>
                <li>Curriculum alignment</li>
                <li>Precision editing</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='experience-block'>
        <div class='job-title'>U-center (Restaurant/Keukenhulp)</div>
        <div class='job-dates'>Aug 2020 – Apr 2022</div>
        <div class='job-summary'>
            My first job was in the kitchen of a mental healthcare clinic.  
            I assisted with food preparation and dishwashing in a fast-paced, high-responsibility environment — while also learning to communicate with diverse groups of people.
            <br><br>
            <strong>Skills developed:</strong>
            <ul class='skills'>
                <li>Teamwork</li>
                <li>Work ethic under pressure</li>
                <li>Responsibility and reliability</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Sidebar
st.sidebar.header("📇 Contact")
st.sidebar.write("📍 6351EK, Bocholtz")
st.sidebar.write("📞 +31 0623042382")
st.sidebar.write("✉️ sebasvansluijsdam@gmail.com")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/sebas-van-sluijsdam-2704svs/)")
