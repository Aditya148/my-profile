import streamlit as st
import time

with st.sidebar:
    with st.spinner("Loading..."):
        time.sleep(3)
    # st.success("Done!")
# Set the title of the app
st.title("My Portfolio")

# Create a sidebar.
st.sidebar.markdown("""
<style>
.sidebar {
  background-color: #333;
  color: white;
  padding: 20px;
}
</style>
""")

# Add a list of links to the sidebar.
st.sidebar.markdown("""
<ul>
  <li><a href="https://www.linkedin.com/in/[Your LinkedIn Profile URL]">LinkedIn</a></li>
  <li><a href="https://github.com/[Your GitHub Username]">GitHub</a></li>
  <li><a href="https://twitter.com/[Your Twitter Username]">Twitter</a></li>
</ul>
""")

# Set the width of the sidebar.
# st.sidebar.width(200)

# Add an image to the app
st.image("assets/images/profile.jpg", width=100)

tab1, tab2, tab3 = st.tabs(["Home", "Contact", "Projects"])

with tab1:
	st.header("Home")
	# Add a section for your education
	st.header("Education")
	st.markdown("""
	I graduated from the University of California, Berkeley with a Bachelor of Science degree in Computer Science. I also have a Master of Science degree in Data Science from Stanford University.
	""")
    # Add a section for your work experience
	st.header("Work Experience")
	st.markdown("""
	I have worked as a data scientist at Google for the past two years. I have also worked as a research assistant at the University of California, Berkeley.
	""")
    # Add a section for your skills
	st.header("Skills")
	st.markdown("""
	I am proficient in Python, R, and SQL. I am also familiar with a variety of machine learning and data science techniques.
	""")

with tab2:
	st.header("Contact")
	# Add a call to action
	st.header("Contact Me")
	st.markdown("""
	If you would like to learn more about my work, please contact me at [email protected] or [phone number].""")

with tab3:
	st.header("Projects")
	# Add a section for your projects
	st.header("Projects")
	st.markdown("""
	I have worked on a variety of projects, including:

	* Developed a machine learning model to predict customer churn
	* Built a data pipeline to collect and analyze data from a variety of sources
	* Created a dashboard to visualize data
	""")

