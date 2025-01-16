import pyautogui
import time

# Fail-safe: Quickly move your mouse to any corner of the screen to stop the script
pyautogui.FAILSAFE = True


def execute_sequence():
    # Get current mouse position to help you find coordinates
    # print(f"Current mouse position: {pyautogui.position()}")

    # Click at your specific position (replace x and y with your coordinates)
    pyautogui.click(x=1083, y=1027)  # Replace these numbers with your coordinates

    # Switch to second tab
    pyautogui.hotkey('ctrl', '3')
    time.sleep(0.2)

    # Press right arrow
    pyautogui.press('down')
    time.sleep(0.2)

    # Press right arrow
    pyautogui.press('left')
    time.sleep(0.2)

    # Copy
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)

    # Switch to second tab
    pyautogui.hotkey('ctrl', '2')
    time.sleep(0.2)

    # Switch to third tab
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)

    # Switch to second tab
    pyautogui.hotkey('ctrl', '3')
    time.sleep(0.2)

    # Press right arrow
    pyautogui.press('right')
    time.sleep(0.2)

    # Switch to third tab
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)

    # Switch to second tab
    pyautogui.hotkey('ctrl', '2')
    time.sleep(0.2)

    # Press tab
    pyautogui.press('tab')
    time.sleep(0.2)

    # Press tab
    pyautogui.press('tab')
    time.sleep(0.2)

    # Press tab
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)

if __name__ == "__main__":
    print(f"Mouse position: {pyautogui.position()}")

    # Run the sequence
    execute_sequence()
