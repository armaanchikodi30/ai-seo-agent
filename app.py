import time
import streamlit as st
from agent import SEOAgent

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI SEO Agent",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.stButton>button {
    width:100%;
    height:55px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    background:#0E76FD;
    color:white;
    border:none;
}

.stButton>button:hover{
    background:#0059d6;
    color:white;
}

.metric-card{
    background:#f8f9fa;
    padding:18px;
    border-radius:12px;
    text-align:center;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🚀 AI SEO Agent")

    st.markdown("---")

    st.subheader("Workflow")

    st.success("✓ Crawl Website")
    st.success("✓ Business Analysis")
    st.success("✓ Competitor Analysis")
    st.success("✓ Keyword Planning")
    st.success("✓ SEO Strategy")
    st.success("✓ Final Report")

    st.markdown("---")

    st.info(
        """
        **Built using**
        - LangChain
        - OpenAI
        - Python
        - Streamlit
        """
    )

# -----------------------------
# Header
# -----------------------------
st.title("🔍 AI SEO Agent")

st.write(
    "Generate AI-powered SEO reports, competitor analysis, keyword planning and SEO strategies."
)

st.divider()

# -----------------------------
# Top Metrics
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="metric-card">
            <h3>🌐 Website Analysis</h3>
            Analyze any website
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="metric-card">
            <h3>📈 SEO Insights</h3>
            AI Generated
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="metric-card">
            <h3>🏆 Competitor Research</h3>
            Automatic
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

# -----------------------------
# URL Input
# -----------------------------
with st.container(border=True):

    st.subheader("Website Analysis")

    website = st.text_input(
        "Website URL",
        placeholder="https://example.com"
    )

    analyze = st.button(
        "🚀 Analyze Website",
        use_container_width=True
    )

# -----------------------------
# Run Agent
# -----------------------------
if analyze:

    if website.strip() == "":
        st.warning("Please enter a website URL.")
        st.stop()

    progress = st.progress(0)

    status = st.empty()

    try:

        status.info("🚀 Initializing AI SEO Agent...")
        progress.progress(10)
        time.sleep(0.4)

        status.info("🌐 Crawling Website...")
        progress.progress(25)
        time.sleep(0.5)

        status.info("🧠 Running Business Analysis...")
        progress.progress(45)
        time.sleep(0.5)

        status.info("📊 Performing Competitor Analysis...")
        progress.progress(60)
        time.sleep(0.5)

        status.info("🔑 Planning Keywords...")
        progress.progress(75)
        time.sleep(0.5)

        status.info("📈 Generating SEO Strategy...")
        progress.progress(90)

        agent = SEOAgent()

        report = agent.run(website)

        progress.progress(100)

        status.success("✅ SEO Analysis Completed!")

        st.balloons()

        st.divider()

        tab1, tab2 = st.tabs(["📄 SEO Report", "📋 Raw Output"])

        with tab1:

            if isinstance(report, dict):

                for key, value in report.items():

                    with st.expander(
                        key.replace("_", " ").title(),
                        expanded=True
                    ):

                        if isinstance(value, list):

                            for item in value:
                                st.markdown(f"- {item}")

                        elif isinstance(value, dict):
                            st.json(value)

                        else:
                            st.write(value)

            else:
                st.markdown(report)

        with tab2:

            if isinstance(report, dict):
                st.json(report)
            else:
                st.code(report)

        st.download_button(
            label="⬇ Download Report",
            data=str(report),
            file_name="seo_report.txt",
            mime="text/plain",
            use_container_width=True
        )

    except Exception as e:

        st.error(f"❌ {e}")