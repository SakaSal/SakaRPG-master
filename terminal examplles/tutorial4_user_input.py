import curses
import time
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)

    # gets ordinal value
    # key = stdscr.getch()
    # gets key
    key = stdscr.getkey()
    stdscr.addstr(5, 5, f"key: {key}")
    stdscr.refresh()
    stdscr.getch()


def main2(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)
    stdscr.nodelay(True)

    x, y = 0, 0
    string_x = 0
    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key == "KEY_LEFT":
            x -= 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_UP":
            y -= 1
        elif key == "KEY_DOWN":
            y += 1

        stdscr.clear()
        string_x += 1
        # stdscr.addstr(0, string_x // 50, "hello world")
        stdscr.addstr(y, x, "0")
        stdscr.refresh()


wrapper(main2)
