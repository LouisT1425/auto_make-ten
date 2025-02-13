import keyboard
import pyautogui

from solver import solve_all

def main():
    print("---Press ctrl+space to start auto solving.---\n")
    print("---Press q to exit.---")
    while not keyboard.is_pressed('q'):
        if keyboard.is_pressed('ctrl+space'):
            solve_all()

if __name__ == '__main__':
    main()
