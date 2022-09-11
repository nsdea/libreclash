import os
# go to the correct path (this file's folder)
os.chdir(os.path.dirname(__file__)) # this is really important and should be done first
os.chdir('..')

import flask
import logging

import helpers

from game.game import game_bp
from home.home import home_bp

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = flask.Flask(__name__, static_url_path='/static', static_folder='static/')
helpers.setup(app)

app.register_blueprint(game_bp)
app.register_blueprint(home_bp)

app.run(port=1230, debug=True)
