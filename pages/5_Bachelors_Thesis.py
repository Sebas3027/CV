import streamlit as st

# Page config
st.set_page_config(page_title="Bachelor Thesis", layout="wide")

# Custom styling
st.markdown("""
    <style>
        .stApp {
            background-image: url("https://www.transparenttextures.com/patterns/graphy.png");
            background-size: contain;
        }
        .thesis-block {
            background-color: rgba(255, 255, 255, 0.95);
            padding: 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        .thesis-title {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .thesis-sub {
            font-size: 18px;
            color: #555;
            margin-bottom: 1.5rem;
        }
        .thesis-section {
            margin-bottom: 1.8rem;
        }
    </style>
""", unsafe_allow_html=True)

# Thesis content block
st.markdown("<div class='thesis-block'>", unsafe_allow_html=True)

st.markdown("<div class='thesis-title'>Bachelor Thesis – EOG Artifact Removal from EEG</div>", unsafe_allow_html=True)
st.markdown("<div class='thesis-sub'>Sebas van Sluijsdam | BSc Data Science & Artificial Intelligence – Maastricht University</div>", unsafe_allow_html=True)

st.markdown("""
<div class='thesis-section'>
<h4>Context</h4>
Eye movements introduce strong artifacts in EEG recordings, known as electrooculogram (EOG) noise. These artifacts can distort or obscure true brain signals, especially in frontal EEG channels.  
This thesis explores and compares two advanced signal decomposition methods to detect and remove EOG artifacts while preserving meaningful EEG information:
<ul>
<li><b>Multivariate Empirical Mode Decomposition (MEMD)</b> – a data-driven method that adaptively decomposes multichannel signals.</li>
<li><b>Canonical Polyadic Decomposition (CPD)</b> – a tensor-based factorization technique that separates signal components via low-rank approximation.</li>
</ul>
</div>

<div class='thesis-section'>
<h4>Research Objectives</h4>
The goal was to systematically compare MEMD and CPD in their ability to:
<ul>
<li>Remove EOG artifacts from multichannel EEG signals</li>
<li>Preserve signal integrity (true brain activity)</li>
<li>Test various CPD configurations for optimal results</li>
</ul>
</div>

<div class='thesis-section'>
<h4>Methodology</h4>
A semi-simulated dataset was constructed by injecting real EOG recordings into clean EEG signals.  
The evaluation was based on two key metrics:
<ul>
<li><b>RRMSE</b> – to quantify noise suppression quality</li>
<li><b>Correlation Coefficient</b> – to assess how well the original EEG structure is preserved</li>
</ul>
For CPD, several grouping strategies were compared, including grouping by frequency, energy, and kurtosis. Different rank and embedding parameters were also tested.
</div>

<div class='thesis-section'>
<h4>Key Findings</h4>
<ul>
<li>MEMD consistently achieved higher correlation with the clean signal, indicating better signal preservation.</li>
<li>CPD showed stronger performance in RRMSE, suggesting more aggressive noise removal.</li>
<li>Grouping by frequency produced the best results among CPD variants, outperforming groupings by energy or kurtosis.</li>
</ul>
</div>

<div class='thesis-section'>
<h4>Skills and Techniques Applied</h4>
Python programming, NumPy, signal processing, tensor decomposition, scientific evaluation, data visualization, academic writing.
</div>
""", unsafe_allow_html=True)
with open("Tensor_decomposition.pdf", "rb") as f:
    pdf_data = f.read()

st.download_button(
    label="📄 Download full thesis (PDF)",
    data=pdf_data,
    file_name="Bachelor_Thesis_Sebas_van_Sluijsdam.pdf",
    mime="application/pdf"
)

st.markdown("</div>", unsafe_allow_html=True)

# Sidebar contact
st.sidebar.header("📇 Contact")
st.sidebar.write("📍 6351EK, Bocholtz")
st.sidebar.write("📞 +31 0623042382")
st.sidebar.write("✉️ sebasvansluijsdam@gmail.com")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/sebas-van-sluijsdam-2704svs/)")
