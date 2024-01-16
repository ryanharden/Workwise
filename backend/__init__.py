import os
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager
from .models import db, User

# Import routes
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .api.workspace_routes import workspace_routes
from .api.project_routes import project_routes

from .seeds import seed_commands
from .config import Config

# Creating an app instance of the import Flask class to represent the application. "__name__" is the global variable for the main module of the application.
app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'

# This callback is used to reload the user object from the user ID stored in the session. It should take the str ID of a user, and return the corresponding user object.
# @login.user_loader modifies the load_user function so that Flask-Login knows to call this function to get the User object corresponding to the user ID stored in the session.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Tell flask about our seed commands
app.cli.add_command(seed_commands)

# Tells the flask instance what configurations we want to use
app.config.from_object(Config)

app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(workspace_routes, url_prefix='/api/workspaces')
app.register_blueprint(project_routes, url_prefix='/api/projects')



# Initializes SQLAlchemy with the flask app
db.init_app(app)

# Integrates Flask-Migrate with your Flask app and SQLAlchemy ORM, enabling it to handle database migrations.
Migrate(app, db)

# Application Security
CORS(app)

# Since we are deploying with Docker and Flask,
# we won't be using a buildpack when we deploy to Heroku.
# Therefore, we need to make sure that in production any
# request made over http is redirected to https.
# Well.........
@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)

# Injects a csrf_token in each response to the client in order to prevent csrf attacks
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get('FLASK_ENV') == 'production' else None,
        httponly=True)
    return response

# Provides us with an output of all routes, their urls, methods, and doc strings you provide
@app.route("/api/docs")
def api_help():
    """
    Returns all API routes and their doc strings
    """
    acceptable_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    route_list = { rule.rule: [[ method for method in rule.methods if method in acceptable_methods ],
                    app.view_functions[rule.endpoint].__doc__ ]
                    for rule in app.url_map.iter_rules() if rule.endpoint != 'static' }
    return route_list


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    """
    This route will direct to the public directory in our
    react builds in the production environment for favicon
    or index.html requests
    """
    if path == 'favicon.ico':
        return app.send_from_directory('public', 'favicon.ico')
    return app.send_static_file('index.html')

# This setup ensures that if users enter or are redirected to a path that the backend does not recognize, the frontend application still loads, and the frontend routing logic can then decide what to display (e.g., a custom 404 page).
@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')
