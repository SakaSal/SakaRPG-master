import curses
import time
from curses import wrapper
from pathlib import Path

# Get the directory of the current script
script_dir = Path(__file__).parent

# Construct the absolute path to the map file
map_file = script_dir.parent / "assets" / "ASCII" / "maps" / "map1.txt"
tiles = {}


def map_terminal(stdscr):

    stdscr.clear()

    map_win = curses.newwin(23, 65, 0, 40)
    init_map(map_file, 23, 65, map_win, stdscr)

    x, y = 41, 1

    player = curses.newwin(2, 2, y, x)
    player.bkgd("@", curses.A_BOLD)
    player.refresh()

    while True:
        key = stdscr.getkey()
        if key == "KEY_LEFT":
            x -= 2
            if x <= 41:
                x = 41
        elif key == "KEY_RIGHT":
            x += 2
            if x >= 101:
                x = 101
        elif key == "KEY_UP":
            y -= 1
            if y <= 1:
                y = 1
        elif key == "KEY_DOWN":
            y += 1
            if y >= 20:
                y = 20
        elif key == "Q":
            break

        player.mvwin(y, x)
        stdscr.erase()
        player_position(stdscr, x, y)
        draw_map(map_file, map_win, stdscr)
        player.refresh()


def player_position(stdscr, x, y):
    player_q1_x = player_q4_x = x - 39
    player_q1_y = player_q2_y = y
    player_q2_x = player_q3_x = x - 40
    player_q3_y = player_q4_y = y + 1

    obstacle_q1_x, distance_q1_x = get_right_obstacle(player_q1_x, player_q1_y, 64)
    obstacle_q4_x, distance_q4_x = get_right_obstacle(player_q4_x, player_q4_y, 64)
    obstacle_q2_x, distance_q2_x = get_left_obstacle(player_q2_x, player_q2_y)
    obstacle_q3_x, distance_q3_x = get_left_obstacle(player_q3_x, player_q3_y)

    stdscr.addstr(
        f"{obstacle_q2_x}{distance_q2_x} ({player_q2_x},{player_q2_y}), ({player_q1_x},{player_q1_y}) {distance_q1_x}{obstacle_q1_x} \n{obstacle_q3_x}{distance_q3_x} ({player_q3_x},{player_q3_y}), ({player_q4_x},{player_q4_y}) {distance_q4_x}{obstacle_q4_x}"
    )


def get_right_obstacle(quad_x, quad_y, maplength):
    distance = 0
    for i in range(quad_x + 1, maplength):
        obstacle = tiles[i, quad_y]
        distance += 1
        if obstacle != " ":
            break
    return obstacle, distance


def get_left_obstacle(quad_x, quad_y):
    distance = 0
    for i in reversed(range(quad_x)):
        obstacle = tiles[i, quad_y]
        distance += 1
        if obstacle != " ":
            break
    return obstacle, distance


def init_map(map_file, lines, cols, map_win, stdscr):
    with open(map_file, "r") as f:
        for y in range(lines):
            for x in range(cols):
                char = f.read(1)
                map_win.addstr(char)
                tiles[(x, y)] = char
                time.sleep(0.00005)
                stdscr.refresh()
                map_win.refresh()


def draw_map(map_file, map_win, stdscr):
    map_win.erase()
    with open(map_file, "r") as f:
        char = f.read()
        map_win.addstr(char)
        stdscr.refresh()
        map_win.refresh()


def count_lines_and_chars(filename):
    """
    Reads a text file and counts the number of characters per line.

    Args:
        filename (str): The path to the text file.
    """
    total_lines = 0
    try:
        with open(filename, "r") as file:
            for line_num, line in enumerate(file, 1):
                # Using len(line.rstrip('\r\n')) to exclude newline characters from the count
                char_count = len(line.rstrip("\r\n"))
                print(f"Line {line_num}: {char_count} characters")
            total_lines = line_num  # Set total lines to the last enumerated line number
        print(f"\nTotal lines in the file: {total_lines}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
