
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def build_menu():
    clear_screen()
    print("===================================")
    print("      Build RAT - New Window       ")
    print("===================================")
    input("Press Enter to continue...")

if __name__ == "__main__":
    build_menu()
    