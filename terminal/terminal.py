import curses
import time
from curses import wrapper


def main(stdscr):
    # first integer is the color id
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    # color id is passed to color_pair
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)

    stdscr.clear()
    # numbers are row and column
    """
    stdscr.addstr(10, 10, "hello world", GREEN_AND_BLACK)
    stdscr.addstr(10, 13, "overwrite")
    stdscr.addstr(12, 20, "goodbye world", RED_AND_WHITE | curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()
    """

    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for i in range(0, 50):
        for j in range(0, 50):
            pad.addstr("._", GREEN_AND_BLACK)

    # (curses.LINES -1, curses.ROWS - 1) coordinates of the screen
    # (padrow, padcol, topwinrow, topwincol, botwinrow, botwincol)
    stdscr.clear()
    count = 0
    for i in range(20):
        if count > 9:
            count = 0
        stdscr.addstr(str(count), GREEN_AND_BLACK)
        count += 1

    for i in range(25):
        stdscr.addstr(f"{i}\n", GREEN_AND_BLACK)
        stdscr.refresh()

    y, x = (10, 10)
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

        pad.addstr(y, x, "0", GREEN_AND_BLACK)
        pad.refresh(y - 5, x - 5, 10, 10, 20, 20)


wrapper(main)
