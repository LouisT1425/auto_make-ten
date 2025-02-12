import time
from image_processing import extract_grid_color
from constants import COLOR_MAP
from mouse_actions import drag
from utils import from_case_to_plateau

def find_matching_pairs(number1, number2):
    """Finds the places on the board where the two numbers are side by side, and returns two arrays,
        one with the horizontal matchings and one with the vertical matchings."""
    colors = extract_grid_color()
    matching_horizontal = []
    matching_vertical = []

    for y in range(9):
        for x in range(15):
            if colors[y][x] == COLOR_MAP[str(number1)] and colors[y][x + 1] == COLOR_MAP[str(number2)]:
                matching_horizontal.append((x, y))
            if colors[y][x] == COLOR_MAP[str(number1)] and colors[y + 1][x] == COLOR_MAP[str(number2)]:
                matching_vertical.append((x, y))

    return matching_horizontal, matching_vertical

def solve(number1, number2):
    """Uses the match function to actually solve the game for 2 given numbers."""
    matches = find_matching_pairs(number1, number2)

    if not matches:
        print("Aucune correspondance trouvée.")
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


def solve_all():
    pairs = [(1, 9), (9, 1), (2, 8), (8, 2), (3, 7), (7, 3), (4, 6), (6, 4), (5, 5)]

    print("Solving ...")
    for number1, number2 in pairs:
        solve(number1, number2)
    print("Done!")

