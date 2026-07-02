# import time
# import streamlit as st
# from agent import SEOAgent
#
# # -----------------------------
# # Page Configuration
# # -----------------------------
# st.set_page_config(
#     page_title="AI SEO Agent",
#     page_icon="🚀",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )
#
# # -----------------------------
# # Custom CSS
# # -----------------------------
# st.markdown("""
# <style>
#
# .main {
#     padding-top: 1rem;
# }
#
# .stButton>button {
#     width:100%;
#     height:55px;
#     border-radius:12px;
#     font-size:18px;
#     font-weight:bold;
#     background:#0E76FD;
#     color:white;
#     border:none;
# }
#
# .stButton>button:hover{
#     background:#0059d6;
#     color:white;
# }
#
# .metric-card{
#     background:#f8f9fa;
#     padding:18px;
#     border-radius:12px;
#     text-align:center;
#     box-shadow:0px 2px 8px rgba(0,0,0,0.08);
# }
#
# .block-container{
#     padding-top:2rem;
# }
#
# </style>
# """, unsafe_allow_html=True)
#
# # -----------------------------
# # Sidebar
# # -----------------------------
# with st.sidebar:
#
#     st.title("🚀 AI SEO Agent")
#
#     st.markdown("---")
#
#     st.subheader("Workflow")
#
#     st.success("✓ Crawl Website")
#     st.success("✓ Business Analysis")
#     st.success("✓ Competitor Analysis")
#     st.success("✓ Keyword Planning")
#     st.success("✓ SEO Strategy")
#     st.success("✓ Final Report")
#
#     st.markdown("---")
#
#     st.info(
#         """
#         **Built using**
#         - LangChain
#         - OpenAI
#         - Python
#         - Streamlit
#         """
#     )
#
# # -----------------------------
# # Header
# # -----------------------------
# st.title("🔍 AI SEO Agent")
#
# st.write(
#     "Generate AI-powered SEO reports, competitor analysis, keyword planning and SEO strategies."
# )
#
# st.divider()
#
# # -----------------------------
# # Top Metrics
# # -----------------------------
# col1, col2, col3 = st.columns(3)
#
# with col1:
#     st.markdown(
#         """
#         <div class="metric-card">
#             <h3>🌐 Website Analysis</h3>
#             Analyze any website
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
#
# with col2:
#     st.markdown(
#         """
#         <div class="metric-card">
#             <h3>📈 SEO Insights</h3>
#             AI Generated
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
#
# with col3:
#     st.markdown(
#         """
#         <div class="metric-card">
#             <h3>🏆 Competitor Research</h3>
#             Automatic
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
#
# st.write("")
#
# # -----------------------------
# # URL Input
# # -----------------------------
# with st.container(border=True):
#
#     st.subheader("Website Analysis")
#
#     website = st.text_input(
#         "Website URL",
#         placeholder="https://example.com"
#     )
#
#     analyze = st.button(
#         "🚀 Analyze Website",
#         use_container_width=True
#     )
#
# # -----------------------------
# # Run Agent
# # -----------------------------
# if analyze:
#
#     if website.strip() == "":
#         st.warning("Please enter a website URL.")
#         st.stop()
#
#     progress = st.progress(0)
#
#     status = st.empty()
#
#     try:
#
#         status.info("🚀 Initializing AI SEO Agent...")
#         progress.progress(10)
#         time.sleep(0.4)
#
#         status.info("🌐 Crawling Website...")
#         progress.progress(25)
#         time.sleep(0.5)
#
#         status.info("🧠 Running Business Analysis...")
#         progress.progress(45)
#         time.sleep(0.5)
#
#         status.info("📊 Performing Competitor Analysis...")
#         progress.progress(60)
#         time.sleep(0.5)
#
#         status.info("🔑 Planning Keywords...")
#         progress.progress(75)
#         time.sleep(0.5)
#
#         status.info("📈 Generating SEO Strategy...")
#         progress.progress(90)
#
#         agent = SEOAgent()
#
#         report = agent.run(website)
#
#         progress.progress(100)
#
#         status.success("✅ SEO Analysis Completed!")
#
#         st.balloons()
#
#         st.divider()
#
#         tab1, tab2 = st.tabs(["📄 SEO Report", "📋 Raw Output"])
#
#         with tab1:
#
#             if isinstance(report, dict):
#
#                 for key, value in report.items():
#
#                     with st.expander(
#                         key.replace("_", " ").title(),
#                         expanded=True
#                     ):
#
#                         if isinstance(value, list):
#
#                             for item in value:
#                                 st.markdown(f"- {item}")
#
#                         elif isinstance(value, dict):
#                             st.json(value)
#
#                         else:
#                             st.write(value)
#
#             else:
#                 st.markdown(report)
#
#         with tab2:
#
#             if isinstance(report, dict):
#                 st.json(report)
#             else:
#                 st.code(report)
#
#         st.download_button(
#             label="⬇ Download Report",
#             data=str(report),
#             file_name="seo_report.txt",
#             mime="text/plain",
#             use_container_width=True
#         )
#
#     except Exception as e:
#
#         st.error(f"❌ {e}")






import time
import streamlit as st

from agent import SEOAgent

# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(
    page_title="AI SEO Agent",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "report" not in st.session_state:
    st.session_state.report = None

if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

# ----------------------------------------------------
# CSS
# ----------------------------------------------------

st.markdown("""
<style>

.main{
    background:#f5f7fb;
}

.block-container{
    padding-top:1.8rem;
    padding-bottom:2rem;
}

section[data-testid="stSidebar"]{
    background:#111827;
}

section[data-testid="stSidebar"] *{
    color:white;
}

.stButton>button{
    width:100%;
    height:52px;
    border-radius:10px;
    background:#2563EB;
    color:white;
    border:none;
    font-size:18px;
    font-weight:600;
}

.stButton>button:hover{
    background:#1D4ED8;
    color:white;
}

.metric-box{
    background:white;
    padding:22px;
    border-radius:15px;
    box-shadow:0 3px 15px rgba(0,0,0,.08);
    text-align:center;
}

.metric-title{
    font-size:15px;
    color:#666;
}

.metric-value{
    font-size:30px;
    font-weight:bold;
    color:#2563EB;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.title("🚀 AI SEO Agent")

    st.markdown("---")

    st.subheader("Workflow")

    workflow = [
        "Website Crawl",
        "Technical SEO Audit",
        "Business Analysis",
        "Competitor Analysis",
        "Keyword Planning",
        "SEO Content Plan",
        "Content Gap Analysis",
        "SEO Score Dashboard",
        "LinkedIn Strategy",
        "Final Report"
    ]

    for item in workflow:
        st.success(f"✓ {item}")

    st.markdown("---")

    st.info("""
### Tech Stack

- LangChain
- Google Gemini
- Python
- Streamlit
""")

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title("🔍 AI SEO Agent")

st.caption(
    "AI Powered Website Analysis • Technical SEO • Competitor Intelligence • Keyword Strategy"
)

st.divider()

# ----------------------------------------------------
# Dashboard Cards
# ----------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-title">Modules</div>
        <div class="metric-value">9</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-title">AI Model</div>
        <div class="metric-value">Gemini</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-title">Reports</div>
        <div class="metric-value">AI</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-title">Status</div>
        <div class="metric-value">Ready</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ----------------------------------------------------
# URL Input
# ----------------------------------------------------

with st.container(border=True):

    st.subheader("Analyze Website")

    website = st.text_input(
        "Website URL",
        placeholder="https://example.com"
    )

    analyze = st.button(
        "🚀 Start SEO Analysis",
        use_container_width=True
    )

# ----------------------------------------------------
# Execute Agent
# ----------------------------------------------------

if analyze:

    if website.strip() == "":
        st.warning("Please enter a valid website URL.")
        st.stop()

    progress = st.progress(0)

    status = st.empty()

    try:

        steps = [
            ("🌐 Crawling Website...",10),
            ("🔧 Technical SEO Audit...",20),
            ("🏢 Business Analysis...",35),
            ("🏆 Competitor Analysis...",50),
            ("🔑 Keyword Planning...",65),
            ("📈 SEO Content Strategy...",75),
            ("🔍 Content Gap Analysis...",85),
            ("📊 Calculating SEO Score...",92),
            ("💼 LinkedIn Strategy...",96),
            ("✅ Preparing Report...",100)
        ]

        for text,val in steps:
            status.info(text)
            progress.progress(val)
            time.sleep(.35)

        agent = SEOAgent()

        report = agent.run(website)

        st.session_state.report = report
        st.session_state.analyzed = True

        status.success("SEO Analysis Completed Successfully!")

    except Exception as e:

        st.error(e)

# ----------------------------------------------------
# SEO DASHBOARD
# ----------------------------------------------------

if st.session_state.analyzed:

    report = st.session_state.report

    st.divider()

    st.header("📊 SEO Dashboard")

    # -----------------------------
    # SEO SCORE
    # -----------------------------

    score = report.get("seo_score_dashboard", {})

    st.subheader("Overall SEO Score")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Overall",
            score.get("overall_score", "-")
        )

    with col2:
        st.metric(
            "Technical",
            score.get("technical_score", "-")
        )

    with col3:
        st.metric(
            "Content",
            score.get("content_score", "-")
        )

    with col4:
        st.metric(
            "Keywords",
            score.get("keyword_score", "-")
        )

    with col5:
        st.metric(
            "Competitors",
            score.get("competitor_score", "-")
        )

    st.divider()

    # -----------------------------
    # Technical SEO
    # -----------------------------

    st.subheader("🔧 Technical SEO Audit")

    technical = report.get("technical_seo", {})

    tech_col1, tech_col2 = st.columns(2)

    with tech_col1:

        st.markdown("### Website Health")

        st.json(technical)

    with tech_col2:

        score_value = technical.get(
            "technical_score",
            0
        )

        st.metric(
            "Technical Score",
            score_value
        )

        st.progress(score_value / 100)

        recommendations = technical.get(
            "recommendations",
            []
        )

        if recommendations:

            st.markdown("### Recommendations")

            for item in recommendations:
                st.write("•", item)

    st.divider()

    # -----------------------------
    # Business Analysis
    # -----------------------------

    st.subheader("🏢 Business Analysis")

    business = report.get(
        "business_analysis",
        {}
    )

    left, right = st.columns(2)

    with left:

        st.metric(
            "Company",
            business.get(
                "company_name",
                "-"
            )
        )

        st.metric(
            "Industry",
            business.get(
                "industry",
                "-"
            )
        )

        st.markdown("### Summary")

        st.write(
            business.get(
                "business_summary",
                "-"
            )
        )

    with right:

        st.markdown("### Products")

        for product in business.get(
            "products",
            []
        ):

            st.success(product)

        st.markdown("### Services")

        for service in business.get(
            "services",
            []
        ):

            st.info(service)

        st.markdown("### Target Audience")

        for audience in business.get(
            "target_audience",
            []
        ):

            st.write("•", audience)

    st.divider()

    # ----------------------------------------------------
    # COMPETITOR ANALYSIS
    # ----------------------------------------------------

    st.subheader("🏆 Competitor Analysis")

    competitors = report.get(
        "competitor_analysis",
        {}
    )

    competitor_list = competitors.get("competitors", [])

    if competitor_list:

        for competitor in competitor_list:

            with st.expander(
                    f"🏢 {competitor.get('company_name', 'Unknown Company')}",
                    expanded=False
            ):

                col1, col2 = st.columns(2)

                with col1:

                    st.markdown("### 🌐 Website")

                    website = competitor.get(
                        "website",
                        "-"
                    )

                    if website:
                        st.write(website)

                    st.markdown("### 📖 Business Summary")

                    st.write(
                        competitor.get(
                            "business_summary",
                            "-"
                        )
                    )

                    st.markdown("### 🎯 Why Competitor?")

                    st.info(
                        competitor.get(
                            "why_competitor",
                            "-"
                        )
                    )

                with col2:

                    st.markdown("### 💼 Products / Services")

                    for item in competitor.get(
                            "products_services",
                            []
                    ):
                        st.success(item)

                    st.markdown("### 👥 Target Audience")

                    for audience in competitor.get(
                            "target_audience",
                            []
                    ):
                        st.write("•", audience)

                st.divider()

                left, right = st.columns(2)

                with left:

                    st.markdown("### ⭐ Unique Selling Points")

                    for usp in competitor.get(
                            "unique_selling_points",
                            []
                    ):
                        st.success(usp)

                    st.markdown("### 🚀 SEO Strengths")

                    strengths = competitor.get(
                        "seo_strengths",
                        []
                    )

                    if isinstance(strengths, list):
                        for s in strengths:
                            st.write("✔", s)
                    else:
                        st.write(strengths)

                with right:

                    st.markdown("### ⚠ Weaknesses")

                    for weakness in competitor.get(
                            "weaknesses",
                            []
                    ):
                        st.warning(weakness)

                    st.markdown("### 📈 Content Strategy")

                    st.write(
                        competitor.get(
                            "content_strategy",
                            "-"
                        )
                    )

                st.divider()

                colA, colB = st.columns(2)

                with colA:

                    st.markdown("### ❌ Missing Opportunities")

                    for item in competitor.get(
                            "missing_opportunities",
                            []
                    ):
                        st.error(item)

                with colB:

                    st.markdown("### ✅ Recommendations")

                    for item in competitor.get(
                            "recommendations",
                            []
                    ):
                        st.success(item)

    else:

        st.info("No competitors found.")

    st.divider()

    st.subheader("🔑 Keyword Strategy")

    keywords = report.get(
        "keyword_plan",
        {}
    )

    k1, k2 = st.columns(2)

    with k1:

        st.markdown("### 🎯 Primary Keywords")

        for keyword in keywords.get(
                "primary_keywords",
                []
        ):
            st.success(keyword)

        st.markdown("### 📍 Secondary Keywords")

        for keyword in keywords.get(
                "secondary_keywords",
                []
        ):
            st.info(keyword)

    with k2:

        st.markdown("### 🔥 Long Tail Keywords")

        for keyword in keywords.get(
                "long_tail_keywords",
                []
        ):
            st.write("•", keyword)

        st.markdown("### 💰 High Intent Keywords")

        for keyword in keywords.get(
                "high_intent_keywords",
                []
        ):
            st.warning(keyword)

    st.divider()

    st.subheader("📈 SEO Content Strategy")

    seo = report.get(
        "seo_content_plan",
        {}
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Pillar Pages",
            "Landing Pages",
            "Blogs",
            "FAQs"
        ]
    )

    with tab1:

        for page in seo.get(
                "pillar_pages",
                []
        ):
            st.success(page)

    with tab2:

        for page in seo.get(
                "landing_pages",
                []
        ):
            st.info(page)

    with tab3:

        for blog in seo.get(
                "blog_topics",
                []
        ):
            st.write("📝", blog)

    with tab4:

        for faq in seo.get(
                "faq_topics",
                []
        ):
            st.write("❓", faq)

    st.divider()

    # ----------------------------------------------------
    # CONTENT GAP ANALYSIS
    # ----------------------------------------------------

    st.subheader("🔍 Content Gap Analysis")

    gap = report.get(
        "content_gap_analysis",
        {}
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### ❌ Missing Services")

        for item in gap.get(
                "missing_services",
                []
        ):
            st.error(item)

        st.markdown("### 📄 Missing Pages")

        for item in gap.get(
                "missing_pages",
                []
        ):
            st.warning(item)

        st.markdown("### 🔑 Missing Keywords")

        for item in gap.get(
                "missing_keywords",
                []
        ):
            st.info(item)

    with col2:

        st.markdown("### 💡 Content Opportunities")

        for item in gap.get(
                "content_opportunities",
                []
        ):
            st.success(item)

        st.markdown("### 📈 SEO Opportunities")

        for item in gap.get(
                "seo_opportunities",
                []
        ):
            st.success(item)

    st.divider()

    st.markdown("### ✅ Recommendations")

    for item in gap.get(
            "recommendations",
            []
    ):
        st.success(item)

    st.divider()

    # ----------------------------------------------------
    # LINKEDIN STRATEGY
    # ----------------------------------------------------

    st.subheader("💼 30-Day LinkedIn Strategy")

    linkedin = report.get(
        "linkedin_strategy",
        {}
    )

    tabs = st.tabs([
        "Week 1",
        "Week 2",
        "Week 3",
        "Week 4"
    ])

    weeks = [
        "week1",
        "week2",
        "week3",
        "week4"
    ]

    for tab, week in zip(tabs, weeks):

        with tab:

            posts = linkedin.get(
                week,
                []
            )

            if posts:

                for idx, post in enumerate(posts, start=1):

                    st.info(
                        f"Day {idx}"
                    )

                    if isinstance(post, dict):

                        for key, value in post.items():
                            st.markdown(
                                f"**{key.replace('_', ' ').title()}**"
                            )

                            st.write(value)

                    else:

                        st.write(post)

                    st.divider()

            else:

                st.info("No posts generated.")

    import json

    st.divider()

    st.subheader("📥 Export Report")

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(

            label="⬇ Download JSON Report",

            data=json.dumps(
                report,
                indent=4
            ),

            file_name="seo_report.json",

            mime="application/json",

            use_container_width=True

        )

    with col2:

        st.download_button(

            label="⬇ Download Text Report",

            data=str(report),

            file_name="seo_report.txt",

            mime="text/plain",

            use_container_width=True

        )

    st.divider()

    st.success(
        "🎉 SEO Analysis Completed Successfully!"
    )

    st.caption(
        "Powered by LangChain • Google Gemini • Streamlit"
    )