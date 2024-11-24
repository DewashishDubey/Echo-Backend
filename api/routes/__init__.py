from flask import Flask, jsonify
from api.routes.auth_views import auth_views
from api.routes.blog_views import blog_views

def register_routes(app: Flask):
    @app.route("/ping")
    def health():
        return jsonify({"status": "ok", "message": "pong"}), 200

    app.register_blueprint(auth_views)
    app.register_blueprint(blog_views)
