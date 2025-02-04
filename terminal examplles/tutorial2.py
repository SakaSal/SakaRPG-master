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

    for i in range(100):
        # experiment with removing clear command
        # stdscr.clear()
        color = BLUE_AND_YELLOW

        if i % 4 == 0:
            color = GREEN_AND_BLACK

        stdscr.addstr(f"Count: {i}", color)
        stdscr.refresh()
        time.sleep(0.1)
    stdscr.getch()


wrapper(main)
