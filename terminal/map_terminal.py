import curses
import time
from curses import wrapper
from pathlib import Path

# Get the directory of the current script
script_dir = Path(__file__).parent

# Construct the absolute path to the map file
map_file = script_dir.parent / "ASCII" / "maps" / "map1.txt"
tiles = {}


def main(stdscr):

    stdscr.clear()

    map_win = curses.newwin(23, 64, 0, 40)
    init_map(map_file, 23, 64, map_win, stdscr)

    x, y = 40, 0

    player = curses.newwin(1, 1, y, x)
    player.bkgd("@", curses.A_BOLD)
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
        elif key == "Q":
            break

        player.mvwin(y, x)
        draw_map(map_file, map_win, stdscr)
        player.refresh()


def init_map(map_file, lines, cols, map_win, stdscr):
    with open(map_file, "r") as f:
        for y in range(lines):
            for x in range(cols):
                char = f.read(1)
                map_win.addstr(char)
                tiles[(x, y)] = char
                time.sleep(0.00005)
                stdscr.refresh()
                map_win.refresh()


def draw_map(map_file, map_win, stdscr):
    map_win.erase()
    with open(map_file, "r") as f:
        char = f.read()
        map_win.addstr(char)
        stdscr.refresh()
        map_win.refresh()


wrapper(main)
