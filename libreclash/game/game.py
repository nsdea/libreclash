import sys
sys.path.append('..') # this is important - to make local modules work

import flask

from models import *

game_bp = flask.Blueprint('game_bp',
    __name__,
    template_folder='../'
)

@game_bp.route('/game')
def game():
    return flask.render_template('game/templates/game.html', tiles=Realm().render())