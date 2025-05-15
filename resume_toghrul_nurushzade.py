import streamlit as st

# --- PAGE SETUP ---


about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

skills_qualifications = st.Page(
    "views/skills_qualifications.py",
    title="Skills & Qualifications",
    icon=":material/star:",
)
study = st.Page(
    "views/study.py",
    title="Study",
    icon=":material/school:",
)
experience = st.Page(
    "views/experience.py",
    title="Experience",
    icon=":material/work_history:",
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page, skills_qualifications],
        "Study and Experience": [study, experience],
    }
)


# --- SHARED ON ALL PAGES ---

# --- RUN NAVIGATION ---
pg.run()
