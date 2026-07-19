import base64
from pathlib import Path

import streamlit as st

from workbook_solutions import PRACTICE_TEST_LINKS

# --------------------------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="Notes | SAT Math Resource Hub",
    page_icon="📝",
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
# WORKBOOK SOLUTIONS PAGE LAYOUT
#
# PRACTICE_TEST_LINKS itself lives in workbook_solutions.py (imported
# above) so the link data stays separate from this page's layout code.
# Add a new test number here once its links are added there.
# --------------------------------------------------------------------------
PRACTICE_TEST_NUMBERS = [4, 5, 6, 7, 8, 9, 10]

MODULE_SPECS = [
    {"label": "Module 1", "suffix": "Module_1"},
    {"label": "Module 2 (Higher Difficulty)", "suffix": "Module_2_HD"},
    {"label": "Module 2 (Lower Difficulty)", "suffix": "Module_2_LD"},
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
        Hide Streamlit's automatic multipage navigation, same as the
        other pages, so only the custom sidebar links/buttons show.
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
            margin: 18px 0 10px 0;
        }}

        .page-title {{
            color: {NAVY};
            font-size: 42px;
            font-weight: 800;
            letter-spacing: 0.5px;
        }}

        .page-subtitle {{
            color: #5A6B87;
            font-size: 16px;
            line-height: 1.6;
            margin-top: 4px;
        }}

        /* ---------- Section headers ---------- */
        .notes-section-title {{
            color: {NAVY};
            font-size: 20px;
            font-weight: 700;
            margin: 30px 0 14px 0;
            border-bottom: 3px solid {GOLD};
            display: inline-block;
            padding-bottom: 4px;
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

        /* ---------- Note cards (native Streamlit containers) ---------- */
        div[data-testid="stVerticalBlockBorderWrapper"] {{
            background-color: white;
            border-radius: 10px !important;
            box-shadow: 0 1px 6px rgba(10, 31, 68, 0.08);
        }}

        /*
        Force text color inside note cards regardless of the viewer's
        light/dark theme setting - without this, Streamlit's default
        text color follows the theme, and on dark mode that renders
        light/white text on our white card background (invisible).
        */
        div[data-testid="stVerticalBlockBorderWrapper"] h1,
        div[data-testid="stVerticalBlockBorderWrapper"] h2,
        div[data-testid="stVerticalBlockBorderWrapper"] h3,
        div[data-testid="stVerticalBlockBorderWrapper"] p,
        div[data-testid="stVerticalBlockBorderWrapper"] span,
        div[data-testid="stVerticalBlockBorderWrapper"] label {{
            color: {NAVY} !important;
        }}

        div[data-testid="stVerticalBlockBorderWrapper"] h3 {{
            color: {NAVY} !important;
            font-weight: 700;
        }}

        div[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stCaptionContainer"],
        div[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stCaptionContainer"] * {{
            color: #5A6B87 !important;
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

    if st.button("⭐ Testimonials", key="nav_testimonials_btn"):
        st.switch_page("pages/Testimonials.py")

    # Keep this custom instance of Notes visible as the active page.
    st.markdown(
        '<a class="sidebar-link active" href="#">📝🗒️ Notes</a>',
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
        <div class="page-title">📝🗒️ Notes</div>
        <p class="page-subtitle">
            Practice test solutions, worked out step by step.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# PRACTICE TEST SOLUTIONS
# --------------------------------------------------------------------------
st.markdown(
    '<span class="notes-section-title">📚 Practice Test Solutions</span>',
    unsafe_allow_html=True,
)
st.write("")

for test_number in PRACTICE_TEST_NUMBERS:
    with st.container(border=True):
        st.markdown(f"### Practice Test #{test_number}")
        module_cols = st.columns(3)
        for col, module in zip(module_cols, MODULE_SPECS):
            url = PRACTICE_TEST_LINKS.get(test_number, {}).get(module["suffix"])
            with col:
                st.markdown(f"**{module['label']}**")
                if url:
                    st.link_button(
                        "📄 Open PDF",
                        url,
                        use_container_width=True,
                    )
                else:
                    st.caption("🚧 Coming Soon 🚧")

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
