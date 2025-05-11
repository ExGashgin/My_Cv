import streamlit as st

st.title("Study")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/th_koeln.png", width=150)

with col2:
    st.header("Cologne University of Applied Sciences", anchor=False)
    st.subheader("Master", anchor=False)
    st.write(
        "October 2018 - August 2024",
    )


col3, col4 = st.columns(2, gap="small", vertical_alignment="center")
with col3:
    st.image("./assets/aztu.png", width=150)

with col4:
    st.header("Azerbaijan Technical University", anchor=False)
    st.subheader("Master", anchor=False)
    st.write(
        "September 2016 - July 2018",
    )

col5, col6 = st.columns(2, gap="small", vertical_alignment="center")
with col5:
    st.image("./assets/esgerlik.png", width=150)
with col6:
    st.header("Azerbaijan Defence Ministry", anchor=False)
    st.subheader("Military Service", anchor=False)
    st.write(
        "June 2014 - June 2016",
    )

col5, col6 = st.columns(2, gap="small", vertical_alignment="center")
with col5:
    st.image("./assets/adnsu.png", width=150)
with col6:
    st.header("Azerbaijan State Oil and Industry University", anchor=False)
    st.subheader("Bachelor", anchor=False)
    st.write(
        "September 2010 - July 2014",
    )