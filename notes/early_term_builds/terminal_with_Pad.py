import curses
from curses import wrapper


def main(stdscr):
    #clear the screen
    stdscr.clear()
    v=2
    stdscr.addstr(1, 0, f"[ATTACKER] HP: {15} \n strikes remaining: {3}\n[DEFENDER] HP: {17}\nstrikes remaining: {4}")
    pad = curses.newpad(100, 100)
    stdscr.refresh()
    
    for y in range(0, 99):
        for x in range(0, 99):
            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)

    pad.refresh( 0,0, 5,5, 20,75)
    stdscr.getkey()

wrapper(main)