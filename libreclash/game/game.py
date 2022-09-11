import flask

# from . import xy

game_bp = flask.Blueprint('game_bp',
    __name__,
    template_folder='../'
)

TILES = [
    ['wall_0', 'wall_1', 'wall_2', 'wall_3', 'wall_4', 'wall_5', 'wall_6'],
    ['wall_0', 'wall_1'],
    ['wall_0', 'wall_1'],
    ['wall_0', 'wall_1', 'wall_0', 'wall_0', 'house_6', 'wall_0', 'wall_0', 'wall_3'],
    ['wall_0', 'wall_1'],
    ['wall_0', 'wall_1'],
    ['wall_0', 'wall_1', 'wall_2', 'wall_3'],
    []
]

@game_bp.route('/game')
def game():
    base_tiles = TILES
    tiles = []

    for row in base_tiles:
        new_row = []

        for tile in row:
            if tile:
                category = tile.split('_')[0]
                stage = int(tile.split('_')[1])
                new_row.append(
                    {
                        'src': f'static/art/{category}/{tile}.png',
                        'class': category,
                        'description': f'{category.title()} (Lvl. {stage})' if stage else '',
                    }
                )

        tiles.append(new_row)
        

    return flask.render_template('game/templates/game.html', tiles=tiles)