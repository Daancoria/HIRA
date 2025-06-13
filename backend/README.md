# HIRA Backend - Tech Residency Project
This is the backend service for HIRA (Healthcare Intelligence Resource Assistant). It handles:
- File uploads
- Data ingestion & processing
- KPI analysis
- AI-generated insights
- Firebase authentication
- Secure audit logs

## :hammer_and_wrench: Tech Stack
- Flask (Python 3.11) // Thought it might be easier for you to just stick to python instead of doing JAVA
- SQLAlchemy
- MySQL / SQLite
- Firebase Admin SDK
- GitHub Actions (CI/CD)

## 🗂 Project Structure

hira-backend/
│
├── app/                # Main Flask application code
│   ├── __init__.py     # App factory
│   ├── config.py       # Configuration file
│   ├── models/         # SQLAlchemy models (your tables)
│   ├── routes/         # API routes (organized by resource)
│   ├── services/       # Business logic / NLP / Parsing / AI agents
│   └── utils/          # Helpers: token validators, parsers, loggers
│
├── tests/              # Unit tests
│   └── test_sample.py
│
├── .env.example        # Environment variables template (never commit secrets)
├── .gitignore          # Prevents committing unwanted files
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
└── .github/
    └── workflows/
        └── ci.yml      # GitHub Actions pipeline
