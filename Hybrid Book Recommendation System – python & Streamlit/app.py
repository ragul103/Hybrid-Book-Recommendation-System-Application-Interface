import streamlit as st
import pandas as pd
from model import recommend_books

st.set_page_config(
    page_title="AI Book Recommendation",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style> html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.main {
    background: linear-gradient(to bottom right, #0F172A, #111827);
    color: white;
}

section[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid rgba(255,255,255,0.08);
}

.hero {
    padding: 35px;
    border-radius: 25px;
    background: linear-gradient(135deg,#4F46E5,#7C3AED,#2563EB);
    text-align: center;
    margin-bottom: 35px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.4);
}

.hero h1 {
    color: white;
    font-size: 60px;
    margin-bottom: 10px;
}

.hero p {
    color: #E5E7EB;
    font-size: 18px;
}

.metric-box {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 25px;
}

.metric-box h2 {
    color: white;
    font-size: 22px;
}

.metric-box p {
    color: #9CA3AF;
}

.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 14px;
    border: none;
    background: linear-gradient(135deg,#7C3AED,#2563EB);
    color: white;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0px 8px 20px rgba(99,102,241,0.4);
}

.book-card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 15px;
    text-align: center;
    min-height: 320px;
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 25px;
    transition: 0.3s;
}

.book-card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 10px 25px rgba(99,102,241,0.3);
}

.book-title {
    color: white;
    font-size: 15px;
    font-weight: 700;
    line-height: 1.5;
    margin-top: 15px;
}

.footer {
    text-align: center;
    color: #9CA3AF;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

try:
    image_df = pd.read_csv("books_with_urls.csv")
except:
    image_df = pd.DataFrame(
        columns=['Book-Title', 'Image-URL-M']
    )

st.markdown("""
<div class="hero">
    <h1>📚 AI Book Recommendation</h1>
    <p>
        Personalized recommendations powered by Hybrid AI Filtering
    </p>
</div>
""", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown("""
    <div class="metric-box">
        <h2>🤖 Hybrid AI</h2>
        <p>User + Item + Content Filtering</p>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-box">
        <h2>⚡ Real-Time</h2>
        <p>Fast Recommendation Engine</p>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-box">
        <h2>📈 Smart Ranking</h2>
        <p>Weighted Recommendation Logic</p>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.title("⚙️ Recommendation Settings")

top_n = st.sidebar.slider(
    "Number of Recommendations",
    min_value=5,
    max_value=20,
    value=10
)

user_id = st.number_input(
    "Enter User ID",
    min_value=1,
    step=1
)

if st.button("🚀 Generate Recommendations"):

    with st.spinner("Analyzing user preferences..."):

        recommendations = recommend_books(
            user_id,
            top_n=top_n
        )

    st.success("Recommendations Generated Successfully")

    st.divider()

    cols = st.columns(5)

    for idx, book in enumerate(recommendations):

        col = cols[idx % 5]

        with col:

            st.markdown(
                '<div class="book-card">',
                unsafe_allow_html=True
            )

            img_row = image_df[
                image_df['Book-Title'] == book
            ]

            if not img_row.empty:
                img_url = img_row.iloc[0]['Image-URL-M']
            else:
                img_url = "https://via.placeholder.com/150x220.png?text=No+Image"

            st.image(
                img_url,
                width=150
            )

            st.markdown(
                f"""
                <div class="book-title">
                    {book}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

st.markdown("""
<div class="footer">
    Built with ❤️ using Streamlit | Hybrid Recommendation System
</div>
""", unsafe_allow_html=True)