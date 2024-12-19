
import pyautogui

def take_screenshot(output_file="screenshot.png"):
    screenshot = pyautogui.screenshot()
    screenshot.save(output_file)
    print(f"Screenshot saved as {output_file}")

if __name__ == "__main__":
    take_screenshot()
    