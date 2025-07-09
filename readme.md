# Victim Cybercrime Assistant (Flask)

A web application that enables victims to register and report cybercrime incidents securely and anonymously.

## 🔧 Tech Stack

- Python (Flask)
- SQLite / SQLAlchemy
- Jinja2 Templates
- Bootstrap 5
- Flask-WTF, Flask-Login
- Flask-Migrate


## 🚀 How to Run

```bash
# Step 1: Clone
git clone https://github.com/yourname/victim-cybercrime-assistant-flask
cd victim-cybercrime-assistant-flask

# Step 2: Setup virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows
# or
source venv/bin/activate  # On macOS/Linux

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the app
flask db init
flask db migrate
flask db upgrade
flask run
