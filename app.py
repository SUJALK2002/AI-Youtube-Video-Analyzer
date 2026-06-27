import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="AI YouTube Video Analyzer",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Segoe UI';
}

.main{
    background:#0f0f0f;
    color:white;
}

h1,h2,h3,h4{
    color:white;
}

.hero{
    background:linear-gradient(90deg,#ff0000,#d50000);
    padding:30px;
    border-radius:18px;
    text-align:center;
    color:white;
    box-shadow:0px 5px 20px rgba(255,0,0,.4);
}

.card{
    background:#1e1e1e;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 15px rgba(255,255,255,.05);
    margin-bottom:15px;
}

.stButton>button{
    background:#ff0000;
    color:white;
    border:none;
    border-radius:10px;
    height:55px;
    width:100%;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#cc0000;
    transform:scale(1.02);
}

textarea{
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Sidebar ---------------- #

st.sidebar.image(
    "https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg",
    width=200
)

st.sidebar.title("⚙ Settings")

st.sidebar.info("""
### Features

✅ AI Video Summary

✅ Timestamp Generation

✅ Topic Detection

✅ Learning Points

✅ Key References

✅ Technical Analysis

Powered by **Groq + Agno**
""")

# ---------------- Hero ---------------- #

st.markdown("""
<div class="hero">
<h1>🎥 AI YouTube Video Analyzer</h1>
<h4>Analyze any YouTube video with AI in seconds 🚀</h4>
<p>Summaries • Timestamps • Key Learnings • Topic Breakdown</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------- Agent ---------------- #

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# ---------------- Input ---------------- #

col1, col2 = st.columns([5,1])

with col1:
    video_url = st.text_input(
        "📺 Paste YouTube Video URL",
        placeholder="https://www.youtube.com/watch?v=..."
    )

with col2:
    st.write("")
    st.write("")
    analyze = st.button("🚀 Analyze")

# ---------------- Preview ---------------- #

if video_url:

    if "watch?v=" in video_url:
        video_id = video_url.split("watch?v=")[1].split("&")[0]
        st.video(f"https://www.youtube.com/watch?v={video_id}")

# ---------------- Analysis ---------------- #

if video_url and analyze:

    progress = st.progress(0)

    with st.spinner("🤖 AI is analyzing the video..."):

        for i in range(100):
            progress.progress(i+1)

        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    progress.empty()

    st.success("✅ Analysis Completed!")

    st.divider()

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("🎥 Videos", "1")
    c2.metric("🤖 AI", "Groq")
    c3.metric("⚡ Speed", "Fast")
    c4.metric("📑 Report", "Ready")

    st.divider()

    with st.expander("📋 View Analysis Report", expanded=True):

        st.markdown(response.content)

    st.download_button(
        "📥 Download Report",
        response.content,
        file_name="youtube_analysis.md",
        mime="text/markdown"
    )

# ---------------- Footer ---------------- #

st.write("")
st.write("")
st.markdown("""
---
<center>

Made with ❤️ using

**Streamlit • Groq • Agno • Python**

</center>
""", unsafe_allow_html=True)