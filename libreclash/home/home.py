import sys
sys.path.append('..') # this is important - to make local modules work

import flask

import tools

home_bp = flask.Blueprint('home_bp',
    __name__,
    template_folder='../'
)

@home_bp.route('/')
def home():
    return flask.render_template('home/templates/welcome.html')
