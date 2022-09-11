const tiles = document.querySelectorAll('.tile');
const overlay = document.querySelector('#tile-overlay');
const tile_name = document.querySelector('#current-tile');
const background = document.querySelectorAll('#current-tile');

function unselect() {
    for (const tile of tiles) {
        overlay.style.opacity = 0;
        tile.style.filter = 'drop-shadow(0 0 3px black) drop-shadow(0 0 6px black)';
    }
}

for (const tile of tiles) {
    tile.ondragstart = function() {
        return false;
    };

    tile.onclick = function() {
        unselect();

        tile_name.innerText = tile.title;
        overlay.style.opacity = 1;
        
        tile.style.filter = 'drop-shadow(0 0 1px white) drop-shadow(0 0 1px white)';
    };
}

background.onclick = function() {
    alert(1);
    unselect();
}
