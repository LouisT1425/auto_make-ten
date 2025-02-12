from constants import SCREEN_CONFIG

def from_case_to_plateau(x, y):
    """Translates the coordinates of a case to a pixel tuple to use in the actual game board."""
    coord_x = int(SCREEN_CONFIG["upper_left"][0]) + x * (SCREEN_CONFIG["dx"] + SCREEN_CONFIG["case_width"]) + 10
    coord_y = int(SCREEN_CONFIG["upper_left"][1]) + y * (SCREEN_CONFIG["dy"] + SCREEN_CONFIG["case_height"])

    return coord_x, coord_y
