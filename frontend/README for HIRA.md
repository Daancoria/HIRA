# 🏥 HIRA – Healthcare Intelligence Resource Assistant

HIRA is an AI-powered decision-support system developed as part of the Vikara Health Tech Residency. It assists hospital middle managers in understanding, analyzing, and acting on workforce and performance data to make informed staffing decisions.

## 📌 Project Overview

- **Sponsor:** Vikara Health Solutions  
- **Lead Contact:** Harnish Patel (President)  
- **Team Roles:** Backend Engineer, Frontend Engineer, Data Analyst, Cybersecurity Specialist, QA Engineer  
- **Timeline:** Sprint-based, MVP delivered by Week 8  
- **Primary Tech Stack:** React, Flask, SQLite/MySQL, OpenAI API  

## 🎯 Key Objectives

| Goal | Success Metric |
|------|----------------|
| Data comprehension | Explain 3+ KPIs from uploaded CSVs |
| Root cause detection | AI suggests at least 1 cause per KPI |
| Clarity | >85% clarity in plain-English output |
| Functionality | Working chatbot UI demo with sample data |
| Security | Role-based access (Manager vs Director), simulated HIPAA-aware design |

## 🔍 Core Features

### 1. 📁 Data Upload & Ingestion
- Manual upload of `.csv`, `.xls`, or `.pdf`
- Backend parsing & schema mapping
- Mock datasets used for development/testing

### 2. 📊 KPI Analysis & Comprehension
- Detects patterns, trends, and anomalies
- Root cause analysis using prompt templates or AI
- Sensitivity levels tagged for compliance

### 3. 🗣️ Natural Language Insights
- Outputs business-friendly summaries
- Translates analytics into actionable recommendations
- OpenAI or rule-based generation

### 4. 💬 Chatbot Interface
- React-based assistant
- Accepts free-text queries
- Personalized responses based on role (Manager or Director)

### 5. 🔐 Role-Based Access Control (RBAC)
- Distinct user flows and access restrictions
- Implemented via Firebase/Auth0

### 6. 🛡️ Security & Compliance
- Local-only data use; no real PHI
- IAM simulation, audit logs
- Adheres to HIPAA-aware design principles

## 🧱 Technical Architecture

| Layer        | Stack/Tools |
|--------------|-------------|
| Frontend     | React + TypeScript, Context/Redux |
| Backend      | Python (Flask), REST APIs |
| Authentication | Firebase/Auth0 |
| Database     | SQLite (MVP) or MySQL |
| AI Engine    | Prompt Templates or OpenAI API |
| CI/CD        | GitHub Actions |
| Hosting      | Localhost or Streamlit Cloud (for demo) |

## 🛠️ Installation & Usage

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-org/hira.git
   cd hira
   ```

2. **Backend**
   ```bash
   cd backend
   pip install -r requirements.txt
   flask run
   ```

3. **Frontend**
   ```bash
   cd frontend
   npm install
   npm start
   ```

4. **Demo**
   - Upload a sample `.csv`
   - Log in as a Manager or Director
   - Ask a question via chatbot

## 🔒 Security Notes

- Simulated HIPAA-compliance (no PII/PHI)
- Audit logs and access restrictions implemented
- No external API dependencies without fallback

## 🧪 QA & Testing

- >90% test coverage on core components
- Component and regression testing included
- QA artifacts: test plans, cases, and logs

## 📈 Metrics for Success

- MVP working with mock data
- >85% mentor-rated clarity on AI outputs
- Verified IAM enforcement
- Demo-ready presentation with full team involvement

## 📎 External Resources

- 📊 [Mock Data Repository](https://drive.google.com/drive/folders/1BgphkRggH1NcBhUYtX9wc7qQkHcEzvZl)  
- 📽️ [Pitch Slide Deck](https://docs.google.com/presentation/d/1_XX2fs6HNK5GHVWkSuJDD7CE4jdGBu7Lgr_T3WN1VdM/edit)

## 📃 License

This project is intended for educational and internal demonstration purposes only. Not licensed for commercial deployment.

Names:
Donald Clemons - FE
Daniel Coria - FE
