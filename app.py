import base64
from pathlib import Path

import streamlit as st

# --------------------------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="SAT Math Resource Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSETS = Path(__file__).parent / "assets"
ROCKET_ICON = ASSETS / "rocket_icon.png"
STUDY_GUIDE_PREVIEW = ASSETS / "study_guide_preview.png"
STUDY_GUIDE_PDF = ASSETS / "SAT_Math_Study_Guide.pdf"

NAVY = "#0A1F44"
GOLD = "#F5B700"
LIGHT_BG = "#F7F9FC"


def img_to_base64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


ROCKET_B64 = img_to_base64(ROCKET_ICON)
PREVIEW_B64 = img_to_base64(STUDY_GUIDE_PREVIEW)
PDF_B64 = img_to_base64(STUDY_GUIDE_PDF)

# --------------------------------------------------------------------------
# TOPIC LIST
# --------------------------------------------------------------------------
TOPICS = [
    "Desmos Tutorial",
    "Linear Equations",
    "Exponential Equations",
    "Quadratic Equations",
    "Equation of a Circle",
    "Functions",
    "Equivalent Expressions",
    "Inequalities",
    "Parallel Lines and Transversals",
    "Radians and Degrees",
    "Mean, Median, Mode, Range and Standard Deviation",
    "Radicals and Exponents",
    "Right Triangles",
    "Trigonometry",
    "Areas",
    "Volumes",
    "Surface Areas",
    "Interpreting Graphs",
    "Probability",
    "Percentages",
    "Ratios, Rates and Proportions",
    "Table of Values",
    "Word Problems",
]

# --------------------------------------------------------------------------
# GLOBAL CSS
# --------------------------------------------------------------------------
st.markdown(
    f"""
    <style>
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}

        .stApp {{
            background-color: {LIGHT_BG};
        }}

        .block-container {{
            padding-top: 0rem;
            max-width: 1100px;
        }}

        /* ---------- Header ---------- */
        .site-header {{
            background-color: {NAVY};
            padding: 18px 28px;
            display: flex;
            align-items: center;
            gap: 18px;
            border-radius: 0 0 10px 10px;
            margin-bottom: 28px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.15);
        }}

        .rocket-btn img {{
            width: 52px;
            height: 52px;
            border-radius: 50%;
            border: 2px solid {GOLD};
            cursor: pointer;
            transition: transform 0.2s ease;
        }}

        .rocket-btn img:hover {{
            transform: scale(1.08);
        }}

        .site-title {{
            color: white;
            font-size: 26px;
            font-weight: 700;
            letter-spacing: 0.3px;
            margin: 0;
        }}

        .site-subtitle {{
            color: #C9D3E5;
            font-size: 14px;
            margin: 0;
        }}

        /* ---------- Welcome box ---------- */
        .welcome-box {{
            background-color: white;
            border-left: 6px solid {GOLD};
            padding: 20px 24px;
            border-radius: 8px;
            margin-bottom: 26px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.06);
        }}

        .welcome-box h3 {{
            color: {NAVY};
            margin-top: 0;
        }}

        .welcome-box p {{
            color: #333;
            font-size: 15.5px;
            line-height: 1.55;
        }}

        /* ---------- Study guide card ---------- */
        .guide-card {{
            background-color: white;
            border-radius: 10px;
            padding: 22px;
            box-shadow: 0 1px 6px rgba(0,0,0,0.08);
            margin-bottom: 30px;
        }}

        .guide-card h3 {{
            color: {NAVY};
            margin-top: 0;
        }}

        .guide-thumb {{
            border: 1px solid #ddd;
            border-radius: 6px;
            transition: box-shadow 0.2s ease, transform 0.2s ease;
        }}

        .guide-thumb:hover {{
            box-shadow: 0 4px 14px rgba(0,0,0,0.18);
            transform: translateY(-2px);
        }}

        .guide-link-wrap {{
            text-align: center;
        }}

        .guide-open-btn {{
            display: inline-block;
            margin-top: 14px;
            background-color: {NAVY};
            color: white !important;
            text-decoration: none;
            padding: 10px 22px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 14px;
            transition: background-color 0.2s ease;
        }}

        .guide-open-btn:hover {{
            background-color: #14306e;
        }}

        /* ---------- Section header ---------- */
        .section-title {{
            color: {NAVY};
            font-size: 22px;
            font-weight: 700;
            margin: 10px 0 14px 0;
            border-bottom: 3px solid {GOLD};
            display: inline-block;
            padding-bottom: 4px;
        }}

        /* ---------- Expander styling ---------- */
        div[data-testid="stExpander"] {{
            background-color: white;
            border-radius: 8px;
            border: 1px solid #E3E8F0;
            margin-bottom: 10px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }}

        div[data-testid="stExpander"] summary {{
            font-weight: 600;
            color: {NAVY};
            font-size: 15.5px;
        }}

        .placeholder-box {{
            background-color: #F0F3F9;
            border: 1px dashed #A9B6CC;
            border-radius: 6px;
            padding: 12px 14px;
            color: #5A6B87;
            font-size: 14px;
            margin-bottom: 10px;
        }}

        .resource-label {{
            font-weight: 600;
            color: {NAVY};
            font-size: 13.5px;
            margin-bottom: 4px;
            margin-top: 6px;
        }}

        /* ---------- Sidebar ---------- */
        section[data-testid="stSidebar"] {{
            background-color: {NAVY};
        }}

        section[data-testid="stSidebar"] * {{
            color: white !important;
        }}

        section[data-testid="stSidebar"] .stMarkdown h2 {{
            color: {GOLD} !important;
        }}

        .sidebar-link {{
            display: block;
            padding: 10px 12px;
            margin-bottom: 6px;
            border-radius: 6px;
            color: white !important;
            text-decoration: none;
            font-weight: 500;
            background-color: rgba(255,255,255,0.05);
            transition: background-color 0.2s ease;
        }}

        .sidebar-link:hover {{
            background-color: rgba(245,183,0,0.2);
        }}

        .footer-note {{
            text-align: center;
            color: #8A93A6;
            font-size: 12.5px;
            margin-top: 40px;
            padding-bottom: 20px;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# SIDEBAR (the "sliding navigation" the rocket icon opens)
# --------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 🚀 Navigation")
    st.markdown(
        f"""
        <a class="sidebar-link" href="#study-guide">📘 Study Guide</a>
        <a class="sidebar-link" href="#video-resources">🎬 Video Resources</a>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.caption("Tap the rocket icon in the header to open or close this menu.")

# --------------------------------------------------------------------------
# HEADER (rocket icon click toggles Streamlit's native sidebar via link)
# --------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="site-header">
        <a class="rocket-btn" href="#" onclick="
            const doc = window.parent.document;
            const btn = doc.querySelector('button[kind=header]') ||
                        doc.querySelector('[data-testid=stSidebarCollapsedControl] button') ||
                        doc.querySelector('[data-testid=collapsedControl] button');
            if (btn) {{ btn.click(); }}
            return false;
        ">
            <img src="data:image/png;base64,{ROCKET_B64}" alt="Menu">
        </a>
        <div>
            <p class="site-title">SAT Math Resource Hub</p>
            <p class="site-subtitle">Tutoring materials, videos, and practice — all in one place</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# WELCOME / HOW-TO MESSAGE
# --------------------------------------------------------------------------
st.markdown(
    """
    <div class="welcome-box">
        <h3>Welcome! 👋</h3>
        <p>
        Hi there, and welcome to your SAT Math study space! This page is designed to make review
        simple: start with the study guide preview below, then use the topic menu to find video
        lessons, example problems, and key vocabulary for each concept. Click the rocket icon in
        the top-left corner any time to jump straight to a section using the side menu.
        Below you will find
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# STUDY GUIDE SECTION
# --------------------------------------------------------------------------
st.markdown('<div id="study-guide"></div>', unsafe_allow_html=True)
st.markdown('<span class="section-title">📘 Study Guide</span>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.6])

with col1:
    st.markdown(
        f"""
        <div class="guide-card guide-link-wrap">
            <a href="data:application/pdf;base64,{PDF_B64}" target="_blank">
                <img class="guide-thumb" src="data:image/png;base64,{PREVIEW_B64}" width="100%">
            </a>
            <br>
            <a class="guide-open-btn" href="data:application/pdf;base64,{PDF_B64}" target="_blank">
                Open Full Study Guide
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="guide-card">
            <h3>SAT Math Cram Sheet</h3>
            <p style="color:#333; line-height:1.6;">
            This quick-reference guide covers the core SAT Math formulas and concepts —
            percents, ratios, slope, systems of equations, charts, area and volume,
            angles and triangles, trigonometry, and circles.
            </p>
            <p style="color:#333; line-height:1.6;">
            Click the preview image or the button to open the full document in a new tab.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --------------------------------------------------------------------------
# VIDEO RESOURCES / TOPIC DROPDOWNS
# --------------------------------------------------------------------------
st.markdown('<div id="video-resources"></div>', unsafe_allow_html=True)
st.markdown('<span class="section-title">🎬 Video Resources & Study Material</span>', unsafe_allow_html=True)
st.write("")

for topic in TOPICS:
    with st.expander(topic):
        st.markdown('<div class="resource-label">🎥 YouTube Video Link</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="placeholder-box">Placeholder — insert YouTube link for '
            f'"{topic}" here.</div>',
            unsafe_allow_html=True,
        )

        st.markdown('<div id="example-problems"></div>', unsafe_allow_html=True)
        st.markdown('<div class="resource-label">✏️ Example Problems</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="placeholder-box">Placeholder — insert example problems / worksheet '
            f'link for "{topic}" here.</div>',
            unsafe_allow_html=True,
        )

        st.markdown('<div id="key-words-and-phrases"></div>', unsafe_allow_html=True)
        st.markdown('<div class="resource-label">🔑 Key Words and Phrases</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="placeholder-box">Placeholder — insert key vocabulary '
            f'for "{topic}" here.</div>',
            unsafe_allow_html=True,
        )

st.markdown(
    '<div class="footer-note">SAT Math Resource Hub · Built for focused, guided review</div>',
    unsafe_allow_html=True,
)
