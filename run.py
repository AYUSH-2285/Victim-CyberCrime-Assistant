from app import create_app
from app.auth.models import User
from app.reports.models import Report


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
