from .routes import routes

def init_routes(app):
    app.register_blueprint(routes)