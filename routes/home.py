from flask import Blueprint, render_template, session

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('home.html', usuario_nome = session.get('usuario_nome'))