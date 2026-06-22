from reportlab.platypus import (        #helps to create pdf easily
    SimpleDocTemplate,  # creates a pdf template
    Paragraph,          # used to add text to pdf
    Spacer              # adds empty space between elements
)
from reportlab.lib.styles import getSampleStyleSheet       #styles define how text look


def create_pdf(report):             # accepts one input report

    file = "project_blueprint.pdf"

    doc = SimpleDocTemplate(file)     #creates an empty pdf
    styles = getSampleStyleSheet()

    elements = []                   # This list stores everything that should appear in the PDF     

    elements.append(
        Paragraph(
            "AI Project Architect",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))      # creates empty vertical space

    for line in report.split("\n"):     # breaks report into two line
        elements.append(
            Paragraph(
                line,
                styles["BodyText"]
            )
        )

    doc.build(elements)     # takes all elements and write them in one

    return file