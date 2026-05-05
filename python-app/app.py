from flask import Flask
from src.routes import register_routes
from src.config import Config

app = Flask(__name__)
app.config.from_object(Config)

register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=Config.PORT, debug=Config.DEBUG)
