import win32api, win32con
import time

def drag(x_init, y_init, x_final, y_final):
    """ Simulates a mouse drag."""
    win32api.SetCursorPos((x_init, y_init))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.08)
    win32api.SetCursorPos((x_final, y_final))
    time.sleep(0.08)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
