
import pyperclip

def steal_clipboard():
    clipboard_content = pyperclip.paste()
    print(f"Clipboard content: {clipboard_content}")

if __name__ == "__main__":
    steal_clipboard()
    