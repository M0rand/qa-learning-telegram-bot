from .health import health_bp
from .example import example_bp

def register_routes(app):
    app.register_blueprint(health_bp)
    app.register_blueprint(example_bp, url_prefix="/example")
