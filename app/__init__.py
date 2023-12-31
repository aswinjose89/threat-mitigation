from flask import Flask

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.rag import rag_bp
    app.register_blueprint(rag_bp, url_prefix='/rag')

    from app.poc import poc_bp
    app.register_blueprint(poc_bp, url_prefix='/poc')

    from app.xss import xss_bp
    app.register_blueprint(xss_bp, url_prefix='/xss')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app