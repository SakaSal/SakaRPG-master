import curses
from curses import wrapper


def main(stdscr):
    # initiate colors
    # color for attacker
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    # color for defender
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # color for HP Bar
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_RED)
    
    # set colors
    attacker_color = curses.color_pair(1)
    defender_color = curses.color_pair(3)
    hp_color = curses.color_pair(2)
    
    # test variables
    attacker_hp = 15
    defender_hp = 17
    
    # battle prompt sans HP box
    stdscr.addstr(1, 0, f"[ATTACKER]\nstrikes remaining: {3}\n", attacker_color)
    stdscr.addstr(4, 0, f"[DEFENDER]\nstrikes remaining: {4}", defender_color)
    
    # add HP boxes
    hp_win_attacker = curses.newwin(1, attacker_hp, 1, 11)
    hp_win_attacker.bkgd(' ', hp_color)
    hp_win_attacker.addstr(f" HP:{attacker_hp}")
    
    hp_win_defender = curses.newwin(1, defender_hp, 4, 11)
    hp_win_defender.bkgd(' ', hp_color)
    hp_win_defender.addstr(f"HP: {defender_hp}")
    
    # refresh the windows
    stdscr.refresh()
    hp_win_attacker.refresh()
    hp_win_defender.refresh()
    
    stdscr.getkey()

wrapper(main)