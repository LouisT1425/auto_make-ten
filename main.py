import keyboard
from solver import solve_all

def main():
    while not keyboard.is_pressed('q'):
        if keyboard.is_pressed('ctrl+space'):
            solve_all()

if __name__ == '__main__':
    main()
