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

    pad = curses.newpad(100, 104)
    stdscr.refresh()

    for i in range(104):
        for j in range(26):
            char = chr(65 + j)
            pad.addstr(char, GREEN_AND_BLACK)

    # (curses.LINES -1, curses.ROWS - 1) coordinates of the screen

    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        # (padrow, padcol, topwinrow, topwincol, botwinrow, botwincol )
        pad.refresh(0, i, 5, i, 10, 25 + i)
        time.sleep(0.2)
    stdscr.getch()


wrapper(main)
