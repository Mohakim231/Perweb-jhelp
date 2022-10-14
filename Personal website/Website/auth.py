from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/technology')
def technology():
    return render_template("technology.html")

@auth.route('/science')
def science():
    return render_template("science.html")

@auth.route('/cosmetics')
def cosmetics():
    return render_template("cosmetics.html")

@auth.route('/about')
def about():
    return render_template("about.html")