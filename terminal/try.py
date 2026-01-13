
from pathlib import Path

# Get the directory of the current script
script_dir = Path(__file__).parent

# Construct the absolute path to the map file
map_file = script_dir.parent / "assets" / "ASCII" / "maps" / "map1.txt"

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
        return total_lines, char_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
count_lines_and_chars(map_file)
