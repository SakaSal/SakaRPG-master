import curses
from curses import wrapper

from .fight import return_damage, roll_attacks


def fight_terminal(stdscr, attacker, defender):
    # initiate colors
    # color for attacker
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    # color for defender
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # color for HP Bar
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_RED)
    # color for fight
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_YELLOW)

    # set colors
    attacker_color = curses.color_pair(1)
    defender_color = curses.color_pair(3)
    hp_color = curses.color_pair(2)
    fight_color = curses.color_pair(4)

    # get HP
    attacker_hp = attacker.atribs["hp"]
    defender_hp = defender.atribs["hp"]

    # roll attacks
    attacker_strikes, defender_strikes = roll_attacks(attacker, defender, "melee")

    # get damage
    attacker_damage, defender_damage = return_damage(attacker, defender, "melee")

    # battle prompt sans HP box
    stdscr.addstr(1, 0, "[FIGHT]", fight_color)
    stdscr.addstr(
        3, 0, f"[ATTACKER]\nstrikes remaining: {attacker_strikes}\n", attacker_color
    )
    stdscr.addstr(
        6, 0, f"[DEFENDER]\nstrikes remaining: {defender_strikes}\n", defender_color
    )

    # add HP boxes
    hp_win_attacker = curses.newwin(1, attacker_hp, 3, 11)
    hp_win_attacker.bkgd("=", hp_color)
    hp_win_attacker.addstr(f" HP: {attacker_hp}")

    hp_win_defender = curses.newwin(1, defender_hp, 6, 11)
    hp_win_defender.bkgd("=", hp_color)
    hp_win_defender.addstr(f" HP: {defender_hp}")

    # refresh the windows
    stdscr.refresh()
    hp_win_attacker.refresh()
    hp_win_defender.refresh()

    stdscr.getkey()
