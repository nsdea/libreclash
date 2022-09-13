
# How realms look like at the beginning of a game
DEFAULT_STRUCTURE = [
    ['wall_0', 'wall_1', 'wall_2', 'wall_3', 'wall_4', 'wall_5', 'wall_6'],
    ['wall_0', 'wall_1'],
    ['wall_0', 'wall_1'],
    ['wall_0', 'wall_1', 'wall_0', 'wall_0', 'house_6', 'wall_0', 'wall_0', 'wall_3'],
    ['wall_0', 'wall_1'],
    ['wall_0', 'wall_1'],
    ['wall_0', 'wall_1', 'wall_2', 'wall_3'],
    []
]

class Realm:
    def __init__(self):
        pass

    def render(self) -> str:
        """Renders the HTML code for the realm."""
        tiles = []

        for row in DEFAULT_STRUCTURE:
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

        return tiles