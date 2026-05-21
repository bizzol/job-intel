Windows
python -m venv venv
venv\Scripts\activate

Linux/macOS
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
playwright install

job-intel/
│
├── app.py
├── config.py
├── requirements.txt
├── jobs.db
│
├── scrapers/
│   ├── greenhouse.py
│   ├── lever.py
│   └── companies.py
│
├── database/
│   ├── db.py
│   └── schema.sql
│
├── alerts/
│   └── email_alerts.py
│
├── filters/
│   └── scoring.py
│
└── logs/