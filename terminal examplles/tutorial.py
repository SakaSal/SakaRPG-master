import curses
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
    stdscr.addstr(10, 10, "hello world", GREEN_AND_BLACK)
    stdscr.addstr(10, 13, "overwrite")
    stdscr.addstr(12, 20, "goodbye world", RED_AND_WHITE | curses.A_BOLD)
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
