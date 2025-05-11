import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/study.py",
    title="Study",
    icon=":material/school:",
)
project_2_page = st.Page(
    "views/experience.py",
    title="Experience",
    icon=":material/work_history:",
)





# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)


# --- SHARED ON ALL PAGES ---

# --- RUN NAVIGATION ---
pg.run()