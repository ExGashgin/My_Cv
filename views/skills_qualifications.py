import streamlit as st

st.title("Skillls & Qualifications")

st.write("\n")
st.header("Languages", anchor=False)
col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/azerabiajani.png", width=50)
with col2:
    st.image("./assets/turkish.png", width=50)
with col3:
    st.image("./assets/english.webp", width=50)
with col4:
    st.image("./assets/german.webp", width=50)
with col5:
    st.image("./assets/russian.png", width=50)


st.write("\n")
st.header("Hard Skills", anchor=False)
st.subheader("Help Desk Support", anchor=False)
st.write("---")
st.write(
    """
    - Troubleshooting & Problem-Solving : Diagnosing and resolving hardware/software issues efficiently
    - Knowledge of Operating Systems: Familiarity with Windows and macOS.
    - Networking Basics: Understanding IP configurations, VPNs, and connectivity issues.
    - Software & Hardware Support: Installing, configuring, and maintaining applications and devices.
    - Remote Access Tools: Using tools like TeamViewer or AnyDesk to assist users remotely.
    - Ticketing Systems: Managing and tracking user requests through platforms like Jira or ServiceNow.
    """
)

st.subheader("Programming", anchor=False)
st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/sql.png", width=100)

with col2:
    st.write(
        """
        - Writing efficient queries for data retrieval
        - Performing joins, aggregations, and subqueries
        - Designing and normalizing database schemas
        - Working with stored procedures and triggers
        """
    )

st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/python.png", width=100)

with col2:
    st.write(
        """
        - Writing clean, efficient code using Python syntax
        - Data manipulation with pandas, NumPy
        - Data visualization using matplotlib, seaborn
        - Debugging and error handling
        """
    )

st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/html.png", width=100)

with col2:
    st.write(
        """
        - Structuring web pages with HTML
        - Embedding multimedia elements (images, videos, audio)
        - Implementing forms and interactive elements
        - Basic CSS for styling and layout
        """
    )


st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/php.webp", width=100)

with col2:
    st.write(
        """
        - Writing dynamic web applications with PHP
        - Database connectivity using MySQL
        - Integrating third-party APIs
        - Debugging PHP scripts effectively

        """
    )


st.subheader("Data Analyst Skills", anchor=False)
st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/data-visualization.webp", width=100)

with col2:
    st.write(
        """
        - Power BI: Creating interactive dashboards and reports
        - Tableau: Building visualizations and data stories
        - Excel: Creating dynamic dashboards with charts, slicers, and KPIs for interactive reporting 
        """
    )

st.write("---")

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/database.png", width=100)

with col2:
    st.write(
        """
        - Postgres: Advanced SQL queries, data modeling, and performance tuning
        - SQLite: Lightweight database management for local applications
        - MySQL: Database design, indexing, and optimization
        - SQL Server: Data warehousing, ETL processes, and reporting service
        """
    )
    

st.write("\n")
st.header("Soft Skills", anchor=False)
st.write(
    """
    - Communication Skills: Data Storytelling, Active Listening, Presentation Skills
    - Problem-Solving & Critical Thinking: Analytical Thinking, Attention to Detail
    - Collaboration & Teamwork: Cross-functional Communication, Adaptability
    - Time Management & Organization: Prioritization, Multitasking
    
      """
)

CERTIFICATES = {
    "🏆 Analyze Data with Python Skill Path": "https://www.codecademy.com/profiles/java3425545538/certificates/a91cf883da2f48e2b977577646801c81",
    "🏆 Analyze Data with SQL Skill Path": "https://www.codecademy.com/profiles/java3425545538/certificates/5cafb2d937090210d7df3652",
    "🏆 BI Dashboards with Power BI Course": "https://www.codecademy.com/profiles/java3425545538/certificates/1cb76ac48943853ca32c394afeb491c9",
    "🏆 BI Dashboards with Tableau Course": "https://www.codecademy.com/profiles/java3425545538/certificates/050d7cf465567fdd0c9abb1fbf20e269",
    "🏆 Data Fundamentals": "https://www.credly.com/badges/3391a546-b6eb-45c8-ac5a-6b523366b937/linked_in_profile",
    "🏆 Learn SQL Course": "https://www.codecademy.com/profiles/java3425545538/certificates/042a4e5884e3eb6ea1f2a12be6abb851",
    "🏆 Learn Python 3 Course": "https://www.codecademy.com/profiles/java3425545538/certificates/6c152bd262967f8c941c9707ed636bda",
    }

st.write('\n')
st.header("Cerificates")
for project, link in CERTIFICATES.items():
    st.write(f"[{project}]({link})")