# SAT Math Resource Hub

A single-page Streamlit app for organizing SAT Math tutoring resources.

## Folder structure

```
app.py
assets/
  rocket_icon.png              (circular rocket icon used in header)
  study_guide_preview.png      (first-page preview of the study guide)
  SAT_Math_Study_Guide.pdf     (the full study guide, opened on click)
```

## Run locally

```bash
pip install streamlit
streamlit run app.py
```

## What's included

- **Header**: navy blue bar with a circular rocket icon (top left). Clicking it
  toggles Streamlit's built-in sidebar navigation.
- **Sidebar**: quick-jump links to Study Guide, Video Resources, Example
  Problems, and Key Words and Phrases.
- **Welcome message**: instructions for students at the top of the page.
- **Study guide preview**: clickable thumbnail of the first page that opens
  the full PDF in a new tab.
- **Topic dropdowns**: one expander per SAT Math topic, each with placeholder
  spots for a YouTube link, example problems, and key vocabulary — ready for
  you to fill in manually.

## Customizing content

Open `app.py` and look for the `TOPICS` list near the top to add, remove, or
reorder topics. Inside the loop that builds each expander, replace the
placeholder `st.markdown(...)` blocks with your actual YouTube links (e.g.
`st.video("https://youtube.com/...")`) and study material links/text.

To swap in a different study guide, replace `assets/SAT_Math_Study_Guide.pdf`
and regenerate `assets/study_guide_preview.png` from its first page.
