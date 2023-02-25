from datetime import time
from flask import Flask
from flask import request
from flask import g

from blog.report.views import report
from blog.user.views import user


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)

# @app.route('/<string:search>', methods=['GET', 'POST'])
# def index(search: str):
#     # if request.method == 'POST':
#     #     pass
#     # elif request.method == 'GET':
#     #     pass
#
#     name = request.args.get('search', None)
#     return f'Test text {search}'
#
#
# @app.before_request
# def process_before_request():
#     """
#     Sets start_time to `g` object
#     """
#     g.start_time = time()
#
#
# @app.after_request
# def process_after_request(response):
#     """
#     adds process time in headers
#     """
#     if hasattr(g, "start_time"):
#         response.headers["process-time"] = time() - g.start_time
#         return response
#
#
# @app.errorhandler(404)
# def handle_404(error):
#     app.logger.error(error)
#     return 'This is 404 ERROR!!!'
