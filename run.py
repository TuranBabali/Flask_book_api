from api.database import db
from api import create_app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()