from constants import GAME_BOARD_CONFIG

def from_case_to_plateau(x, y):
    """Translates the coordinates of a case to a pixel tuple to use in the actual game board."""
    coord_x = int(GAME_BOARD_CONFIG["upper_left"][0]) + x * (GAME_BOARD_CONFIG["dx"] + GAME_BOARD_CONFIG["case_width"]) + 10
    coord_y = int(GAME_BOARD_CONFIG["upper_left"][1]) + y * (GAME_BOARD_CONFIG["dy"] + GAME_BOARD_CONFIG["case_height"])

    return coord_x, coord_y
