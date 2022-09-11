import flask

# from . import xy

game_bp = flask.Blueprint('game_bp',
    __name__,
    template_folder='../'
)

@game_bp.route('/game')
def game():
    return flask.render_template('game/templates/game.html')