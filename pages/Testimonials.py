import base64
from pathlib import Path

import streamlit as st

# --------------------------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="Testimonials | SAT Math Resource Hub",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Assets folder lives one level up, next to app.py
ASSETS = Path(__file__).parent.parent / "assets"
ROCKET_ICON = ASSETS / "rocket_icon.png"

NAVY = "#0A1F44"
GOLD = "#F5B700"
LIGHT_BG = "#F7F9FC"
SKY_BLUE = "#E8F4FD"


def img_to_base64(path: Path) -> str:
    """Convert an image file to a Base64 string."""
    return base64.b64encode(path.read_bytes()).decode()


ROCKET_B64 = img_to_base64(ROCKET_ICON) if ROCKET_ICON.exists() else None

if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = False


def toggle_sidebar() -> None:
    """Open or close the custom sidebar."""
    st.session_state.sidebar_open = not st.session_state.sidebar_open


# --------------------------------------------------------------------------
# PLACEHOLDER TESTIMONIALS
# Replace the text values below with real student messages later.
# --------------------------------------------------------------------------
TESTIMONIALS = [
    {
        "name": "Student Name",
        "text": "Testimonial placeholder - insert student message here.",
    },
    {
        "name": "Student Name",
        "text": "Testimonial placeholder - insert student message here.",
    },
    {
        "name": "Student Name",
        "text": "Testimonial placeholder - insert student message here.",
    },
    {
        "name": "Student Name",
        "text": "Testimonial placeholder - insert student message here.",
    },
    {
        "name": "Student Name",
        "text": "Testimonial placeholder - insert student message here.",
    },
    {
        "name": "Student Name",
        "text": "Testimonial placeholder - insert student message here.",
    },
]

# --------------------------------------------------------------------------
# SIDEBAR VISIBILITY CSS
# --------------------------------------------------------------------------
if st.session_state.sidebar_open:
    SIDEBAR_VISIBILITY_CSS = """
    section[data-testid="stSidebar"] {
        display: block !important;
        min-width: 260px !important;
        width: 260px !important;
        transform: none !important;
    }
    """
else:
    SIDEBAR_VISIBILITY_CSS = """
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    """

# --------------------------------------------------------------------------
# GLOBAL CSS
# --------------------------------------------------------------------------
st.markdown(
    f"""
    <style>
        #MainMenu {{
            visibility: hidden;
        }}

        footer {{
            visibility: hidden;
        }}

        .stApp {{
            background: linear-gradient(
                180deg,
                {SKY_BLUE} 0%,
                {LIGHT_BG} 55%
            );
        }}

        .block-container {{
            padding-top: 1.5rem;
            max-width: 1100px;
        }}

        header[data-testid="stHeader"] {{
            background-color: transparent;
            height: 0rem;
        }}

        header[data-testid="stHeader"] * {{
            visibility: hidden;
        }}

        /*
        Hide Streamlit's automatic multipage navigation.

        This removes the automatic "App" and first "Testimonials" entries,
        while preserving the custom Study Guide, Video Resources, and
        Testimonials links created below.
        */
        section[data-testid="stSidebarNav"],
        div[data-testid="stSidebarNav"] {{
            display: none !important;
        }}

        /* ---------- Custom sidebar toggle button ---------- */
        .main div[data-testid="stButton"] {{
            position: fixed;
            top: 14px;
            left: 14px;
            z-index: 999999;
        }}

        .main div[data-testid="stButton"] button {{
            width: 40px;
            height: 40px;
            padding: 0;
            background-color: {NAVY};
            color: {GOLD};
            border: 2px solid {GOLD};
            border-radius: 8px;
            font-size: 16px;
            font-weight: 700;
            letter-spacing: -2px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
            transition:
                transform 0.15s ease,
                background-color 0.15s ease;
        }}

        .main div[data-testid="stButton"] button:hover {{
            transform: scale(1.06);
            background-color: #14306E;
            color: {GOLD};
            border: 2px solid {GOLD};
        }}

        div[data-testid="stSidebarCollapseButton"],
        button[data-testid="stSidebarCollapseButton"] {{
            display: none !important;
        }}

        {SIDEBAR_VISIBILITY_CSS}

        /* ---------- Header ---------- */
        .site-header {{
            background-color: {NAVY};
            padding: 18px 28px;
            display: flex;
            align-items: center;
            gap: 18px;
            border-radius: 10px;
            margin-bottom: 10px;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.15);
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

        /* ---------- Page title ---------- */
        .page-title-wrap {{
            text-align: center;
            margin: 28px 0 10px 0;
        }}

        .page-title {{
            color: {NAVY};
            font-size: 42px;
            font-weight: 800;
            letter-spacing: 0.5px;
        }}

        .page-title .star {{
            color: {GOLD};
        }}

        .page-subtitle {{
            color: #5A6B87;
            font-size: 16px;
            line-height: 1.6;
            margin-top: 4px;
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
            background-color: rgba(255, 255, 255, 0.05);
            transition: background-color 0.2s ease;
        }}

        .sidebar-link:hover {{
            background-color: rgba(245, 183, 0, 0.2);
        }}

        .sidebar-link.active {{
            background-color: rgba(245, 183, 0, 0.25);
        }}

        /* ---------- Custom sidebar navigation buttons ---------- */
        section[data-testid="stSidebar"] div[data-testid="stButton"] {{
            position: static;
            margin-bottom: 6px;
        }}

        section[data-testid="stSidebar"] div[data-testid="stButton"] button {{
            width: 100%;
            display: block;
            text-align: left;
            padding: 10px 12px;
            border-radius: 6px;
            color: white;
            font-weight: 500;
            font-size: 14px;
            background-color: rgba(255, 255, 255, 0.05);
            border: none;
            box-shadow: none;
            transition: background-color 0.2s ease;
        }}

        section[data-testid="stSidebar"]
        div[data-testid="stButton"] button:hover {{
            background-color: rgba(245, 183, 0, 0.2);
            color: white;
            transform: none;
        }}

        /* ---------- Cloud grid ---------- */
        .cloud-field {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 50px;
            padding: 40px 20px 20px 20px;
        }}

        .cloud-container {{
            width: 240px;
            height: 170px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .cloud {{
            position: relative;
            width: 220px;
            height: 130px;
            background: #FFFFFF;
            border-radius: 100px;
            box-shadow: 0 6px 16px rgba(10, 31, 68, 0.12);
            display: flex;
            align-items: center;
            justify-content: center;
            transition:
                transform 0.3s ease,
                box-shadow 0.3s ease;
            cursor: pointer;
        }}

        .cloud::before {{
            content: "";
            position: absolute;
            background: #FFFFFF;
            border-radius: 100px;
            width: 110px;
            height: 110px;
            top: -55px;
            left: 20px;
        }}

        .cloud::after {{
            content: "";
            position: absolute;
            background: #FFFFFF;
            border-radius: 100px;
            width: 90px;
            height: 90px;
            top: -45px;
            right: 25px;
        }}

        .cloud:hover {{
            transform: scale(1.1);
            box-shadow: 0 10px 24px rgba(10, 31, 68, 0.2);
        }}

        .cloud-text {{
            position: relative;
            z-index: 5;
            width: 78%;
            text-align: center;
            color: #5A6B87;
            font-size: 13px;
            font-style: italic;
            line-height: 1.4;
        }}

        .cloud-name {{
            position: relative;
            z-index: 5;
            display: block;
            margin-top: 6px;
            color: {NAVY};
            font-size: 12.5px;
            font-weight: 700;
            font-style: normal;
        }}

        /* ---------- Rocket send-off section ---------- */
        .rocket-section {{
            background-color: {NAVY};
            border-radius: 16px;
            margin: 50px auto 30px auto;
            padding: 40px 30px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 34px;
            flex-wrap: wrap;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
            position: relative;
            overflow: hidden;
        }}

        .rocket-visual {{
            font-size: 70px;
            animation: float-rocket 2.6s ease-in-out infinite;
        }}

        @keyframes float-rocket {{
            0% {{
                transform: translateY(0) rotate(-4deg);
            }}

            50% {{
                transform: translateY(-16px) rotate(4deg);
            }}

            100% {{
                transform: translateY(0) rotate(-4deg);
            }}
        }}

        .rocket-message {{
            max-width: 480px;
            color: white;
        }}

        .rocket-message h3 {{
            color: {GOLD};
            margin: 0 0 8px 0;
            font-size: 20px;
        }}

        .rocket-message p {{
            margin: 0;
            font-size: 15px;
            line-height: 1.6;
            color: #E3E8F0;
        }}

        .footer-note {{
            text-align: center;
            color: #8A93A6;
            font-size: 12.5px;
            margin-top: 30px;
            padding-bottom: 20px;
        }}

        /* ---------- Mobile responsiveness ---------- */
        @media (max-width: 700px) {{
            .block-container {{
                padding-left: 1rem;
                padding-right: 1rem;
            }}

            .site-header {{
                padding: 16px 18px;
            }}

            .site-title {{
                font-size: 21px;
            }}

            .site-subtitle {{
                font-size: 12px;
            }}

            .page-title {{
                font-size: 34px;
            }}

            .cloud-field {{
                gap: 38px;
                padding-left: 0;
                padding-right: 0;
            }}
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# SIDEBAR
# --------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 🚀 Navigation")

    if st.button("📘 Study Guide", key="nav_study_guide_btn"):
        st.switch_page("app.py")

    if st.button("🎬 Video Resources", key="nav_video_resources_btn"):
        st.switch_page("app.py")

    # Keep this custom instance of Testimonials visible.
    st.markdown(
        '<a class="sidebar-link active" href="#">⭐ Testimonials</a>',
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.caption(
        "Use the arrow button in the top-left corner to open or close this menu."
    )

# --------------------------------------------------------------------------
# CUSTOM SIDEBAR TOGGLE BUTTON
# --------------------------------------------------------------------------
st.button(
    "»›",
    key="sidebar_toggle_btn",
    on_click=toggle_sidebar,
)

# --------------------------------------------------------------------------
# HEADER
# --------------------------------------------------------------------------
if ROCKET_B64:
    header_icon_html = (
        f'<img src="data:image/png;base64,{ROCKET_B64}" '
        f'style="width:52px;height:52px;border-radius:50%;'
        f'border:2px solid {GOLD};" '
        f'alt="SAT Math Resource Hub">'
    )
else:
    header_icon_html = '<span style="font-size:40px;">🚀</span>'

st.markdown(
    f"""
    <div class="site-header">
        <div>{header_icon_html}</div>

        <div>
            <p class="site-title">SAT Math Resource Hub</p>
            <p class="site-subtitle">
                Tutoring materials, videos, and practice — all in one place
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# PAGE TITLE
# --------------------------------------------------------------------------
st.markdown(
    """
    <div class="page-title-wrap">
        <div class="page-title">
            <span class="star">⭐</span> Testimonials
        </div>

        <p class="page-subtitle">
            See What’s Possible with the Right Support.<br>
            Read Real Stories from Real Students.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# CLOUD TESTIMONIALS
# --------------------------------------------------------------------------
clouds_html = '<div class="cloud-field">'

for testimonial in TESTIMONIALS:
    clouds_html += f"""
        <div class="cloud-container">
            <div class="cloud">
                <div class="cloud-text">
                    “{testimonial["text"]}”
                    <span class="cloud-name">
                        — {testimonial["name"]}
                    </span>
                </div>
            </div>
        </div>
    """

clouds_html += "</div>"

st.markdown(clouds_html, unsafe_allow_html=True)

# --------------------------------------------------------------------------
# ROCKET SEND-OFF SECTION
# --------------------------------------------------------------------------
st.markdown(
    """
    <div class="rocket-section">
        <div class="rocket-visual">🚀</div>

        <div class="rocket-message">
            <h3>To every future student...</h3>

            <p>
                Every expert was once a beginner. Every big score started with
                one small step, one practice problem, and one “aha” moment.
                Keep showing up, keep asking questions, and trust the process.
                You’re capable of more than you know. The sky isn’t the limit;
                it’s just the launch pad. 🌟
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# FOOTER
# --------------------------------------------------------------------------
st.markdown(
    """
    <div class="footer-note">
        SAT Math Resource Hub · Built for focused, guided review
    </div>
    """,
    unsafe_allow_html=True,
)
