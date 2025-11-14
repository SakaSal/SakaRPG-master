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

    # set the in_fight variable
    stdscr.getch()
    in_fight = True

    # start fight loop
    while in_fight==True:
        # battle prompt sans HP box
        stdscr.addstr(1, 0, "[FIGHT]", fight_color)
        stdscr.addstr(
            3, 0, f"[ATTACKER]\nstrikes remaining: {attacker_strikes}\n", attacker_color
        )
        stdscr.addstr(
            6, 0, f"[DEFENDER]\nstrikes remaining: {defender_strikes}\n", defender_color
        )

        # add HP boxes
        hp_bar_attacker = curses.newwin(1, 1 if attacker_hp <= 0 else attacker_hp, 3, 16)
        hp_bar_attacker.bkgd("=", hp_color)
        hp_text_attacker = curses.newwin(1, 6, 3, 11)
        attacker_hp = 0 if attacker_hp <= 0 else attacker_hp
        hp_text_attacker.addstr(f"HP:{attacker_hp}")
        
    
        hp_bar_defender = curses.newwin(1, 1 if defender_hp <= 0 else defender_hp, 6, 16)
        hp_bar_defender.bkgd("=", hp_color)
        hp_text_defender = curses.newwin(1,6,6,11)
        defender_hp = 0 if defender_hp <= 0 else defender_hp
        hp_text_defender.addstr(f"HP:{defender_hp}")


        # fight bar
        fight_bar = curses.newwin(1, 30, 8, 0)
        fight_bar.bkgd("+", fight_color)

        # refresh the windows
        screens = [stdscr, hp_bar_attacker,hp_text_attacker, hp_bar_defender,hp_text_defender, fight_bar]
        refresh_all(screens)

        #start attacker sub-loop
        if attacker_strikes > 0:
            fight_bar.addstr("[ATTACKER]")
            fight_bar.refresh()
            stdscr.addstr(9, 0, f"[1]:Attack [2] Parry\n", attacker_color)
            choice = stdscr.getkey()
            if choice == "1":
                attacker_strikes -= 1
                defender_hp -= attacker_damage
                stdscr.addstr(
                    12,
                    0,
                    f"{attacker.name} strikes a blow dealing {attacker_damage} dmg to {defender.name}, {defender.name}'s hp is {0 if defender_hp <= 0 else defender_hp}",
                )
            if choice == "2":
                attacker_strikes -= 1
                defender_strikes -= 1
                stdscr.addstr(12, 0 , f"{attacker.name} parry's the next attack",)
        if defender_hp <= 0:
            in_fight =False
            break
        
        stdscr.addstr(1, 0, "[FIGHT]", fight_color)
        stdscr.addstr(
            3, 0, f"[ATTACKER]\nstrikes remaining: {attacker_strikes}\n", attacker_color
        )
        stdscr.addstr(
            6, 0, f"[DEFENDER]\nstrikes remaining: {defender_strikes}\n", defender_color
        )

        # add HP boxes
        hp_bar_attacker = curses.newwin(1, 1 if attacker_hp <= 0 else attacker_hp, 3, 16)
        hp_bar_attacker.bkgd("=", hp_color)
        hp_text_attacker = curses.newwin(1,6,3,11)
        attacker_hp = 0 if attacker_hp <= 0 else attacker_hp
        hp_text_attacker.addstr(f"HP:{attacker_hp}")
        
    
        hp_bar_defender = curses.newwin(1, 1 if defender_hp <= 0 else defender_hp, 6, 16)
        hp_bar_defender.bkgd("=", hp_color)
        hp_text_defender = curses.newwin(1,6,6,11)
        defender_hp = 0 if defender_hp <= 0 else defender_hp
        hp_text_defender.addstr(f"HP:{defender_hp}")


        # fight bar
        fight_bar = curses.newwin(1, 30, 8, 0)
        fight_bar.bkgd("+", fight_color)

        # refresh the windows
        screens = [stdscr, hp_bar_attacker,hp_text_attacker, hp_bar_defender,hp_text_defender, fight_bar]
        refresh_all(screens)
        
        #start defender subloop
        if defender_strikes > 0:
            fight_bar.erase()
            fight_bar.addstr("[DEFENDER]")
            fight_bar.refresh()
            stdscr.addstr(9, 0, f"[1]:Attack [2] Parry\n", defender_color)
            choice = stdscr.getkey()
            if choice == "1":
                defender_strikes -= 1
                attacker_hp -= defender_damage
                stdscr.addstr(
                    12,
                    0,
                    f"{defender.name} strikes a blow dealing {defender_damage} dmg to {attacker.name}, {attacker.name}'s hp is {0 if attacker_hp <= 0 else attacker_hp}",
                )
            if choice == "2":
                attacker_strikes -= 1
                defender_strikes -= 1
                stdscr.addstr(12, 0 , f"{defender.name} parry's the next attack",)
        if attacker_hp <= 0:
            in_fight =False
        if defender_strikes == 0 and attacker_strikes ==0:
            in_fight = False
        

            
    
    stdscr.getch()

    curses.endwin()


def refresh_all(screens):
    for screen in screens:
        screen.refresh()


"""
    stdscr.refresh()
    hp_bar_attacker.refresh()
    hp_bar_defender.refresh()
    fight_bar.refresh()
"""
