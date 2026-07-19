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
        "name": "Alexis Class of 26 (Bright Futures Scholar)",
        "text": "Sean is a really knowledgebale and patient tutor. He made me feel comfortable asking questions and created a great learning environment. He made SAT Math a lot easier to understand and always explained problems in different ways until I finally got it. You can tell he really knows the material and cares about helping his students succeed. I would definetly recommend Sean to anyone studying for the SAT because I think you'll see a big improvement in your score.",
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
            margin: 18px 0 2px 0;
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
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            justify-items: center;
            align-items: start;
            gap: 36px 28px;
            max-width: 960px;
            margin: 0 auto;
            padding: 12px 20px 30px 20px;
        }}

        .cloud-container {{
            width: 100%;
            max-width: 300px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .cloud {{
            position: relative;
            width: 100%;
            max-width: 300px;
            height: 210px;
            box-sizing: border-box;
            padding: 26% 15% 16% 15%;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 130'%3E%3Cg fill='%23ffffff'%3E%3Crect x='18' y='55' width='164' height='62' rx='31'/%3E%3Cellipse cx='52' cy='52' rx='40' ry='36'/%3E%3Cellipse cx='100' cy='36' rx='48' ry='42'/%3E%3Cellipse cx='148' cy='52' rx='40' ry='36'/%3E%3Cellipse cx='26' cy='82' rx='26' ry='24'/%3E%3Cellipse cx='174' cy='82' rx='26' ry='24'/%3E%3Cellipse cx='75' cy='95' rx='24' ry='20'/%3E%3Cellipse cx='125' cy='95' rx='24' ry='20'/%3E%3C/g%3E%3C/svg%3E");
            background-size: 100% 100%;
            background-repeat: no-repeat;
            filter: drop-shadow(0 6px 12px rgba(10, 31, 68, 0.18));
            display: flex;
            align-items: center;
            justify-content: center;
            transition:
                transform 0.2s ease,
                filter 0.2s ease;
            cursor: pointer;
        }}

        .cloud:hover {{
            transform: translateY(-7px);
            filter: drop-shadow(0 12px 18px rgba(10, 31, 68, 0.26));
        }}

        .cloud-text {{
            position: relative;
            z-index: 5;
            width: 100%;
            text-align: center;
            color: #3E4C64;
            font-size: 12.5px;
            font-style: italic;
            line-height: 1.55;
            display: -webkit-box;
            -webkit-line-clamp: 6;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}

        .cloud-name {{
            position: relative;
            z-index: 5;
            display: block;
            margin-top: 8px;
            color: {NAVY};
            font-size: 13.5px;
            font-weight: 700;
            font-style: normal;
        }}

        /* ---------- Cloud modal (click a cloud to enlarge it) ---------- */
        .cloud-link {{
            display: block;
            text-decoration: none;
            color: inherit;
        }}

        .cloud-modal-overlay {{
            position: fixed;
            inset: 0;
            z-index: 9999;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            pointer-events: none;
            transition:
                opacity 0.28s ease,
                visibility 0.28s ease;
        }}

        .cloud-modal-overlay:target {{
            opacity: 1;
            visibility: visible;
            pointer-events: auto;
        }}

        .cloud-modal-backdrop {{
            position: absolute;
            inset: 0;
            z-index: 1;
            background: rgba(8, 20, 45, 0.78);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
        }}

        .cloud-modal-content {{
            position: relative;
            z-index: 2;
            max-height: 90vh;
            overflow-y: auto;
            overflow-x: hidden;
            padding: 40px 18px;
            transform: scale(0.82);
            transition: transform 0.28s ease;
        }}

        .cloud-modal-overlay:target .cloud-modal-content {{
            transform: scale(1);
        }}

        .cloud-modal-close {{
            position: fixed;
            top: 20px;
            right: 20px;
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: {NAVY};
            color: {GOLD};
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 16px;
            text-decoration: none;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
            z-index: 3;
        }}

        .cloud.enlarged {{
            width: fit-content;
            max-width: min(92vw, 760px);
            min-width: 320px;
            height: auto;
            min-height: 260px;
            padding: 84px 64px 60px 64px;
            cursor: default;
        }}

        .cloud.enlarged:hover {{
            transform: none;
        }}

        .cloud.enlarged .cloud-text {{
            max-width: 560px;
            margin: 0 auto;
            font-size: 14px;
            line-height: 1.7;
            display: block;
            -webkit-line-clamp: unset;
            overflow: visible;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }}

        .cloud.enlarged .cloud-name {{
            font-size: 15px;
            margin-top: 18px;
        }}

        /* ---------- Rocket send-off section ---------- */
        .rocket-section {{
            background-color: {NAVY};
            border-radius: 16px;
            margin: 26px auto 24px auto;
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
            margin-right: 12px;
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
            margin-top: 18px;
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
                gap: 30px 20px;
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
#
# NOTE: This HTML block must not contain any blank lines. Streamlit's
# Markdown renderer treats a blank line inside a <div>...</div> block as
# the end of the HTML block; anything after it then gets parsed as a
# regular Markdown paragraph/indented-code block instead of HTML, which
# is why tags were showing up as literal text before.
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
# CLOUD TESTIMONIALS + CLICK-TO-ENLARGE MODALS
#
# Each cloud is a link to a hidden full-screen overlay (id="testimonial-N").
# The overlay uses the CSS :target pseudo-class to animate in/out, so no
# JavaScript is required. Everything is built as one concatenated string
# with no blank lines, since Streamlit's Markdown renderer ends an HTML
# block at the first blank line it encounters.
#
# Each modal is placed in the DOM immediately BEFORE its matching card.
# Because the modal is position:fixed (out of normal flow), it isn't
# counted as a grid item, so the visual 2-column grid order is unaffected.
# This ordering lets a plain CSS sibling selector (~) target "the specific
# source card whose modal is currently open" and fade it out, so the
# original small card doesn't show duplicate text behind the enlarged one.
# --------------------------------------------------------------------------
cloud_blocks = []
hide_source_rules = []

for idx, testimonial in enumerate(TESTIMONIALS):
    modal_id = f"testimonial-{idx}"
    source_class = f"cloud-source-{idx}"

    modal_html = (
        f'<div class="cloud-modal-overlay" id="{modal_id}">'
        '<a href="#" class="cloud-modal-backdrop" aria-label="Close testimonial"></a>'
        '<div class="cloud-modal-content">'
        '<a href="#" class="cloud-modal-close" aria-label="Close testimonial">✕</a>'
        '<div class="cloud enlarged">'
        '<div class="cloud-text">'
        f'“{testimonial["text"]}”'
        '<span class="cloud-name">'
        f'— {testimonial["name"]}'
        "</span>"
        "</div>"
        "</div>"
        "</div>"
        "</div>"
    )

    card_html = (
        f'<a href="#{modal_id}" class="cloud-link {source_class}">'
        '<div class="cloud-container">'
        '<div class="cloud">'
        '<div class="cloud-text">'
        f'“{testimonial["text"]}”'
        '<span class="cloud-name">'
        f'— {testimonial["name"]}'
        "</span>"
        "</div>"
        "</div>"
        "</div>"
        "</a>"
    )

    cloud_blocks.append(modal_html + card_html)

    hide_source_rules.append(
        f"#{modal_id}:target ~ .{source_class} {{ "
        "opacity: 0; visibility: hidden; transition: opacity 0.2s ease; "
        "}}"
    )

hide_source_css = (
    '<style>' + "".join(hide_source_rules) + '</style>'
)

clouds_html = (
    hide_source_css
    + '<div class="cloud-field">'
    + "".join(cloud_blocks)
    + "</div>"
)

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
