import streamlit as st
from forms.contact import contact_form

st.markdown('[Azerbaijani Version](https://toghrul-nurushzade-resume-aze.streamlit.app/)', unsafe_allow_html=True)

@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.png", width=230)

with col2:
    st.title("Toghrul Nurushzade", anchor=False)
    st.subheader("IT Specialist", anchor=False)
    if st.button("✉️ Contact Me"):
        show_contact_form()


col3, col4, col5, col6, col7 = st.columns(5, gap="small", vertical_alignment="center")
with col3:
    st.markdown('<a href="mailto:toghrul.nur@gmail.com" target="_blank">Gmail</a>', unsafe_allow_html=True)

with col4:
    st.markdown('<a href="https://www.linkedin.com/in/toghrulnurushzade/" target="_blank">LinkedIn</a>', unsafe_allow_html=True)

with col5:
    st.markdown('<a href="https://github.com/ExGashgin" target="_blank">Github</a>', unsafe_allow_html=True)

with col6:
    st.markdown('<a href="https://www.facebook.com/exgashgin/" target="_blank">Facebook</a>', unsafe_allow_html=True)

with col7:
    st.markdown('<a href="https://www.instagram.com/n_togrul_n/" target="_blank">Instagram</a>', unsafe_allow_html=True)


# --- ABOUT ME ---
st.write("\n")
st.subheader("Summary", anchor=False)
st.write("---")
st.write(
    """
    Results-driven IT specialist transitioning into a Data Analyst role, 
    with a strong foundation in programming, database management, and business 
    intelligence. Proficient in Python, SQL, Power BI, and data visualization 
    techniques to extract meaningful insights and optimize decision-making. 
    Experienced in handling large datasets, troubleshooting IT infrastructure, 
    and supporting cross-functional teams. Adept at problem-solving, structured analysis, 
    and leveraging technical expertise to enhance operational efficiency. Eager to apply 
    data-driven methodologies to solve business challenges and drive strategic growth.
    """

)
