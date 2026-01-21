import curses


def colors():
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_RED)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_BLUE)

    color_dict = {
        "blue_black": curses.color_pair(1),
        "black_blue": curses.color_pair(5),
        "green_black": curses.color_pair(3),
        "cyan_red": curses.color_pair(2),
        "red_yellow": curses.color_pair(4),
    }

    return color_dict
