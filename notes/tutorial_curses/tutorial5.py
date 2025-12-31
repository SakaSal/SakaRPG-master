import curses
from curses import wrapper
from curses.textpad import rectangle

# this is called by the wrapper
stdscr = curses.initscr()


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    GREEN_AND_BLACK = curses.color_pair(2)
    RED_AND_WHITE = curses.color_pair(3)
    curses.echo()

    stdscr.attron(RED_AND_WHITE)
    stdscr.border()
    stdscr.attroff(RED_AND_WHITE)

    stdscr.attron(BLUE_AND_YELLOW)
    rectangle(stdscr, 1, 1, 5, 20)
    stdscr.attroff(BLUE_AND_YELLOW)
    stdscr.addstr(5, 30, "hello sal")

    stdscr.move(10, 30)

    stdscr.refresh()

    while True:
        key = stdscr.getkey()
        if key == "2":
            break

    curses.endwin()


wrapper(main)
