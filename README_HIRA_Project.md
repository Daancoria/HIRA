
# HIRA – Healthcare Intelligence Resource Assistant

HIRA is an AI-powered decision-support chatbot designed to help hospital managers analyze staffing data and make informed workforce decisions.

---

## 🔧 Tech Stack

- **Frontend:** React + TypeScript
- **Backend:** Flask (Python)
- **Database:** MySQL (via SQLAlchemy)
- **AI Integration:** OpenAI API (GPT-3.5 / GPT-4)
- **Auth:** Firebase (for user login and role-based access)
- **Hosting:** Localhost or cloud (Render/Vercel/Netlify for FE, Flask-compatible for BE)

---

## 📁 Project Structure

```
/hirafrontend         # React frontend
/backend              # Flask backend
/app/blueprints       # Modular route handlers (users, kpi, uploads, ai_response, etc.)
/uploads              # For uploaded files (CSV, XLS, etc.)
.env                  # Environment config (never commit this!)
```

---

## ✅ Features

- Upload staffing data (.csv, .xls, .pdf)
- Ask natural-language questions to analyze KPIs
- GPT-based responses with insight summaries
- Role-based dashboards (Manager vs Director)
- Export chat history, file upload support
- Swagger API docs (`/api/docs`)

---

## 🚀 Setup Instructions

### 1. Clone the Repo
```
git clone https://github.com/your-org/hira.git
cd hira
```

### 2. Setup Backend
```
cd backend
python -m venv venv
venv\Scripts\activate   # or `source venv/bin/activate`
pip install -r requirements.txt
```

Add a `.env` file:
```
FLASK_APP=app
FLASK_ENV=development
DATABASE_URI=mysql+pymysql://user:password@localhost/hira_db
SECRET_KEY=your_secret_key
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

Run the backend:
```
flask run
```

### 3. Setup Frontend
```
cd hirafrontend
npm install
npm run dev
```

To switch from mock to real GPT backend:
Edit `src/services/chatbotService.ts`:
```
const USE_MOCK = false;
```

---

## 🔄 API Endpoint Example

`POST /analyze`
```json
{
  "prompt": "What are my staffing gaps this week?"
}
```

Response:
```json
{
  "reply": "You're overstaffed by 1.5 FTEs in MedSurg."
}
```

---

## 📄 Docs & Resources

- Product Requirements: See PRD.pdf
- Visual Flow: See Visual Diagram.docx
- Integration Guide: See GPT_API_MVP_Integration_Guide.docx

---

## 👥 Team Roles

- **Frontend:** React UI, chat interface, auth handling
- **Backend:** File parsing, AI routes, DB integration
- **Data Analyst:** EDA, mock datasets, KPIs
- **Cybersecurity:** RBAC, endpoint security, HIPAA simulation
- **QA:** Testing workflows, validation logic

---

## 📬 Contact

Project by Vikara Health Solutions | Built by Coding Temple Tech Residency 38 Team HIRA 
