# 🚀 AI Project Architect

**AI Project Architect** is a beginner-friendly Python application that generates complete AI project blueprints based on a project domain, difficulty level, and preferred technologies. The application helps learners and developers quickly plan AI projects and download the generated blueprint as a PDF report.

---

## ✨ Features

* 🎯 Generate AI project ideas based on a selected domain
* 📚 Choose project difficulty:

  * Beginner
  * Intermediate
  * Advanced
* 💻 Specify technologies to use
* 🤖 Automatically create a detailed project blueprint
* 📄 Export the blueprint as a professional PDF report
* 🌐 Simple and interactive Streamlit interface

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Groq API**
* **ReportLab**
* **python-dotenv**

---

## 📁 Project Structure

```text
AI_Project_Architect/
│
├── app.py                  # Streamlit application
├── architect.py            # AI blueprint generation logic
├── report_generator.py     # PDF report generation
├── requirements.txt        # Project dependencies
├── .env                    # API keys (not pushed to GitHub)
├── .gitignore
├── assets/
└── project_blueprint.pdf
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/AI_Project_Architect.git
cd AI_Project_Architect
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/Mac**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add your API key:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

## 📖 How It Works

1. Enter the project domain.
2. Select the project difficulty level.
3. Specify technologies to use.
4. Click **Generate Blueprint**.
5. Review the generated AI project plan.
6. Download the blueprint as a PDF report.

---

## 📄 Generated Blueprint Includes

* Project Title
* Problem Statement
* Objectives
* Features
* System Architecture
* Recommended Tech Stack
* Dataset Suggestions
* Implementation Steps
* Folder Structure
* Future Enhancements

---

## 🎯 Learning Outcomes

This project demonstrates:

* Building AI-powered applications using APIs
* Prompt engineering and content generation
* Developing web applications with Streamlit
* PDF report generation using ReportLab
* Environment variable management
* Modular Python programming

---

## 👩‍💻 Author

**Bhakti Jadhav**

Aspiring Python Developer | AI & ML Learner | Building Projects One Step at a Time

⭐ If you found this project useful, consider giving it a star on GitHub!
