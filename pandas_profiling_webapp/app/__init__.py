import os

from flask import Flask, request, session

app = Flask(__name__, instance_relative_config=True, template_folder="views")
app.config["SECRET_KEY"] = "secret"

con = None

with app.app_context():
    from .routes import *
