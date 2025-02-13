import pyautogui
from constants import GAME_BOARD_CONFIG

def capture_case():
    """Outdated. Captures every case of the game board and returns them as a screenshot array."""
    coord_x, coord_y = GAME_BOARD_CONFIG["upper_left"]
    screenshots = [[]]

    for y in range(10):
        for x in range(16):
            screenshot = pyautogui.screenshot(region=(coord_x, coord_y, GAME_BOARD_CONFIG["case_width"], GAME_BOARD_CONFIG["case_height"]))
            coord_x += GAME_BOARD_CONFIG["dx"] + GAME_BOARD_CONFIG["case_width"]
            screenshots[y].append(screenshot)
        coord_x = GAME_BOARD_CONFIG["upper_left"][0]
        coord_y += GAME_BOARD_CONFIG["dy"] + GAME_BOARD_CONFIG["case_height"]
        screenshots.append([])

    return screenshots

def capture_plateau():
    """Captures the game board and returns it as a screenshot."""
    x, y = GAME_BOARD_CONFIG["upper_left"]
    width = GAME_BOARD_CONFIG["upper_right"][0] - x
    height = GAME_BOARD_CONFIG["bottom_left"][1] - y

    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    return screenshot

def extract_grid_color():
    """Gets the RGB value of every case of the game board and returns them as an array."""
    screenshot = capture_plateau()
    width, height = screenshot.size

    color_tab = []
    pixel_start_x = 39
    pixel_start_y = 29
    step_x = 50
    step_y = 50

    for y in range(10):
        row = []
        pixel_coord_y = pixel_start_y + y * step_y

        if pixel_coord_y >= height:
            print(f"Avertissement : pixel_coord_y={pixel_coord_y} dépasse height={height}")
            break

        for x in range(16):
            pixel_coord_x = pixel_start_x + x * step_x

            if pixel_coord_x >= width:
                print(f"Avertissement : pixel_coord_x={pixel_coord_x} dépasse width={width}")
                break

            row.append(screenshot.getpixel((pixel_coord_x, pixel_coord_y)))

        color_tab.append(row)

    return color_tab
