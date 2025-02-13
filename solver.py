import time
from image_processing import extract_grid_color
from constants import COLOR_MAP
from mouse_actions import drag
from utils import from_case_to_plateau

def find_pairs():
    """Finds the places on the board where two numbers adding to 10 are side by side,
    and returns two arrays: one with horizontal matchings and one with vertical matchings."""

    colors = extract_grid_color()
    matching_horizontal = []
    matching_vertical = []

    for y in range(10):
        for x in range(16):
            try:
                n1 = list(COLOR_MAP.keys())[list(COLOR_MAP.values()).index(colors[y][x])]

                if x + 1 < 16:
                    n2_h = list(COLOR_MAP.keys())[list(COLOR_MAP.values()).index(colors[y][x + 1])]
                    if int(n1) + int(n2_h) == 10:
                        matching_horizontal.append((x, y))

                if y + 1 < 10:
                    n2_v = list(COLOR_MAP.keys())[list(COLOR_MAP.values()).index(colors[y + 1][x])]
                    if int(n1) + int(n2_v) == 10:
                        matching_vertical.append((x, y))

            except ValueError:
                continue

    return matching_horizontal, matching_vertical


def solve_pairs():
        """Uses the match function to actually solve the game for 2 given numbers."""
        matches = find_pairs()

        if not matches:
            print("Found no pairs !")
            return

        horizontal_matches = matches[0]
        vertical_matches = matches[1]

        for x, y in horizontal_matches:
            drag(from_case_to_plateau(x, y)[0],
                 from_case_to_plateau(x, y)[1],
                 from_case_to_plateau(x + 1, y)[0],
                 from_case_to_plateau(x + 1, y)[1]
                 )
            time.sleep(0.1)

        for x, y in vertical_matches:
            drag(from_case_to_plateau(x, y)[0],
                 from_case_to_plateau(x, y)[1],
                 from_case_to_plateau(x, y + 1)[0],
                 from_case_to_plateau(x,y +1)[1]
                 )
            time.sleep(0.1)

def find_squares():
    """Trouve les carrés de 2x2 dont la somme est 10"""
    colors = extract_grid_color()
    squares = []

    for y in range(9):
        for x in range(15):
            try:
                n1 = list(COLOR_MAP.keys())[list(COLOR_MAP.values()).index(colors[y][x])]
                n2 = list(COLOR_MAP.keys())[list(COLOR_MAP.values()).index(colors[y][x + 1])]
                n3 = list(COLOR_MAP.keys())[list(COLOR_MAP.values()).index(colors[y + 1][x])]
                n4 = list(COLOR_MAP.keys())[list(COLOR_MAP.values()).index(colors[y + 1][x + 1])]

                if int(n1) + int(n2) + int(n3) + int(n4) == 10:
                    squares.append((x, y))
            except ValueError:
                continue

    return squares


def solve_squares():
    squares = find_squares()

    if not squares:
        print("Found no squares !")
        return

    for x, y in squares:
        drag(from_case_to_plateau(x, y)[0],
             from_case_to_plateau(x, y)[1],
             from_case_to_plateau(x + 1, y + 1)[0],
             from_case_to_plateau(x + 1, y + 1)[1]
             )
        time.sleep(0.1)

def find_non_adjacent_pairs():
    """Finds pairs of numbers that sum to 10, ignoring empty cells in between them."""

    colors = extract_grid_color()
    matching_horizontal = []
    matching_vertical = []

    for y in range(10):
        for x in range(16):
            try:
                n1 = list(COLOR_MAP.keys())[list(COLOR_MAP.values()).index(colors[y][x])]

                i = 1
                while x + i < 16:
                    n2 = list(COLOR_MAP.keys())[list(COLOR_MAP.values()).index(colors[y][x + i])]

                    if int(n2) != 0:
                        if int(n1) + int(n2) == 10:
                            matching_horizontal.append((x, x + i, y))
                        break
                    i += 1

                j = 1
                while y + j < 10:
                    n2 = list(COLOR_MAP.keys())[list(COLOR_MAP.values()).index(colors[y + j][x])]

                    if int(n2) != 0:
                        if int(n1) + int(n2) == 10:
                            matching_vertical.append((x, y, y + j))
                        break
                    j += 1

            except ValueError:
                continue

    print("horiz : " + str(matching_horizontal) + "\nvert : "  + str(matching_vertical))
    return matching_horizontal, matching_vertical

def solve_non_adjacent_pairs():

    pairs = find_non_adjacent_pairs()
    horizontal_matches = pairs[0]
    vertical_matches = pairs[1]

    for x, x_dest, y in horizontal_matches:
        drag(from_case_to_plateau(x, y)[0],
             from_case_to_plateau(x, y)[1],
             from_case_to_plateau(x_dest, y)[0],
             from_case_to_plateau(x_dest, y)[1])
        time.sleep(0.1)

    for x, y, y_dest in vertical_matches:
        drag(from_case_to_plateau(x, y)[0],
             from_case_to_plateau(x, y)[1],
             from_case_to_plateau(x, y_dest)[0],
             from_case_to_plateau(x, y_dest)[1])
        time.sleep(0.1)
        time.sleep(0.1)

def solve_all():

    print("Solving ...")
    solve_pairs()
    solve_squares()
    solve_non_adjacent_pairs()
    print("Done!")

