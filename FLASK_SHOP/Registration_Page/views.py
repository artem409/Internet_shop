import flask
from shop.settings import db
from .models import User

def render():
    if flask.request.method == 'POST':
        print(flask.request.form)
        user = User(
            name = flask.request.form['name'],
            email = flask.request.form['email'],
            password = flask.request.form['password']
        )
        db.session.add(user)
        db.session.commit()
    return flask.render_template(template_name_or_list = "shop.html")
        
        