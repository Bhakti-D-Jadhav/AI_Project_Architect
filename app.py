import streamlit as st                      # used to create web interface
from architect import generate_project
from report_generator import create_pdf     # imports the create pdf function from report generation

st.set_page_config(                         # sets the page settings
    page_title="AI Project Architect",
    page_icon="🏗️",
    layout="wide"                           # makes the webpage use the entire screen width
)

st.title("🏗️ AI Project Architect")        
st.caption(     
    "Generate complete AI project blueprints"
)

domain = st.text_input(                     # creates a textbox
    "Project Domain",
    placeholder="Domain of project"
)

level = st.selectbox(                       # creates a dropdown
    "Difficulty",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

tech = st.text_input(                   # textbox to write the used technologies
    "Technologies",
    placeholder="Write technologies to use"
)

if st.button("🚀 Generate Blueprint"):          # generates an clickable button

    with st.spinner(                            # shows loading button
        "Designing your project..."
    ):

        report = generate_project(              # calls the function
            domain,
            level,
            tech
        )

        st.markdown(report)                     # display report on the webpage

        pdf = create_pdf(report)                # calls create_pdf(report)
        with open(pdf, "rb") as f:              # opens pdf file
            st.download_button(                 # creates a button download pdf
                "📄 Download PDF",
                f,
                "project_blueprint.pdf"
            )
