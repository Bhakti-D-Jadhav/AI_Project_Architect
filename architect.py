from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_project(domain, level, tech):      # project accepts three input

    prompt = f"""
Create an AI project blueprint.

Domain: {domain}
Difficulty: {level}
Technologies: {tech}

Return the response in proper Markdown format.

Rules:
- Use # for Project Title
- Use ## for section headings
- Use bullet points using -
- Use **bold** where necessary
- Keep the formatting clean and professional
- keep folder structure in image

Generate:
1. Project Title
2. Problem Statement
3. Features
4. Tech Stack
5. Folder Structure
6. Future Enhancements
"""

    response = client.chat.completions.create(          # sends prompt to AI model
        model="llama-3.3-70b-versatile",
        messages=[                                      
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content          # extracts the text