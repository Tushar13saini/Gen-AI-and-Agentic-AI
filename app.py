import streamlit as st 

st.set_page_config(page_title="Cinema Curator AI", layout="wide")

# -------------------- DATA --------------------
movies = [
    {
        "title": "Parasite",
        "genre": "Thriller, Drama",
        "score": 92,
        "desc": "An original and masterfully directed social commentary.",
        "image": "https://via.placeholder.com/400x200"
    },
    {
        "title": "The Grand Budapest Hotel",
        "genre": "Comedy, Adventure",
        "score": 88,
        "desc": "Unique visual style and witty dialogue.",
        "image": "https://via.placeholder.com/400x200"
    },
    {
        "title": "Spirited Away",
        "genre": "Animation, Fantasy",
        "score": 85,
        "desc": "Critically acclaimed animated masterpiece.",
        "image": "https://via.placeholder.com/400x200"
    },
    {
        "title": "Whiplash",
        "genre": "Drama, Music",
        "score": 90,
        "desc": "Intense and powerful performance-driven story.",
        "image": "https://via.placeholder.com/400x200"
    }
]

# -------------------- CSS --------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}

.movie-card {
    background: rgba(255,255,255,0.05);
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 20px;
    transition: 0.3s;
}

.movie-card:hover {
    transform: scale(1.02);
    box-shadow: 0px 4px 20px rgba(255,255,255,0.1);
}

.title {
    color: #FFC107;
    font-size: 22px;
    font-weight: bold;
}

.score {
    color: #00ffcc;
    font-weight: bold;
}

.tag {
    display: inline-block;
    background: #2E4053;
    color: #fff;
    padding: 4px 8px;
    border-radius: 6px;
    margin-right: 5px;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.title("🎬 Cinema Curator AI")
st.write("AI-powered personalized movie recommendations")

# -------------------- HERO --------------------
st.markdown("## 🌟 Featured Movie: The Grand Budapest Hotel")
st.image("https://via.placeholder.com/1200x300", use_container_width=True)
st.write("A lavish visual masterpiece full of style and storytelling.")

st.divider()

# -------------------- MOVIE SECTION --------------------
st.subheader("🔥 AI Recommended Movies")

for m in movies:
    st.markdown(f"""
    <div class="movie-card">
        <img src="{m['image']}" width="100%" style="border-radius:10px;">
        <p class="title">{m['title']}</p>
        <p>
            <span class="tag">{m['genre']}</span>
        </p>
        <p class="score">Match Score: {m['score']}%</p>
        <p>{m['desc']}</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------- TRENDING --------------------
st.divider()
st.subheader("📈 Trending Movies")

trending = [
    {"title": "Dune: Part Two", "genre": "Sci-Fi", "score": "High"},
    {"title": "Past Lives", "genre": "Romance", "score": "Growing"}
]

for t in trending:
    st.write(f"🎬 **{t['title']}** | {t['genre']} | Popularity: {t['score']}")