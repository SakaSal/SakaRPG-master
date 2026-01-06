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


count_lines_and_chars(r"E:\gits\sakarpg\SakaRPG-master\notes\trypy\map1.txt")
