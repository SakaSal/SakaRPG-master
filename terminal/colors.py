import curses


def colors():
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    # color for defender
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # color for HP Bar
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_RED)
    # color for fight
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_YELLOW)

    color_dict = {
        "blue_black": curses.color_pair(1),
        "green_black": curses.color_pair(3),
        "cyan_red": curses.color_pair(2),
        "red_yellow": curses.color_pair(4),
    }

    return color_dict
