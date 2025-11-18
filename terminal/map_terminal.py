import curses
import time
from curses import wrapper
from pathlib import Path

# Get the directory of the current script
script_dir = Path(__file__).parent

# Construct the absolute path to the map file
map_file = script_dir.parent / "ASCII" / "maps" / "map1.txt"


def main(stdscr):

    stdscr.clear()
    tiles = {}
    map_win = curses.newwin(23, 64, 0, 40)
    with open(map_file, "r") as f:

        for y in range(23):
            for x in range(64):
                char = f.read(1)
                map_win.addstr(char)
                tiles[(x, y)] = char
                # time.sleep(0.001)
                stdscr.refresh()
                map_win.refresh()

    x, y = 40, 0

    player = curses.newwin(1, 1, y, x)
    player.bkgd("@", curses.A_BOLD)
    player.refresh()
    player.erase()
    player.refresh()
    while True:

        key = stdscr.getkey()

        if key == "KEY_LEFT":
            x -= 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_UP":
            y -= 1
        elif key == "KEY_DOWN":
            y += 1

        player.clear()
        player.refresh()
        player.mvwin(y, x)
        player.refresh()
        stdscr.refresh()
        map_win.refresh()

    print(tiles[(10, 3)])
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
