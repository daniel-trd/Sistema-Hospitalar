from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models.models import db
from routes.routes import bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)
app.register_blueprint(bp)
for r in app.url_map.iter_rules():
    print(r.endpoint, "->", r.rule)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

