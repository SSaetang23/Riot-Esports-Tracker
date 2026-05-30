from flask import Blueprint, render_template

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
def index():
    return "<h1>Esports Tracker is running!</h1>"