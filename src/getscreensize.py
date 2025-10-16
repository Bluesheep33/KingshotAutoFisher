import pyautogui

def wait_for_click(prompt):
    print(prompt)
    print("Position your mouse and press Enter to capture position...")
    input()  # Wait for Enter key press
    return pyautogui.position()

def get_emulator_screen_size():
    top_left = wait_for_click("Move your mouse to the TOP-LEFT corner of your emulator window.")
    bottom_right = wait_for_click("Move your mouse to the BOTTOM-RIGHT corner of your emulator window.")
    width = bottom_right.x - top_left.x
    height = bottom_right.y - top_left.y
    print(f"Emulator screen size: {width}x{height}, Top-Left: {top_left}")
    return width, height, top_left
