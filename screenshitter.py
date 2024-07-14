import os
import time
import threading
from pynput import keyboard, mouse
import pyautogui

# Directory to save screenshots
screenshot_dir = "screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

# Flag to control the listening state
running = False

def take_screenshot():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
    pyautogui.screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

def on_press(key):
    global running
    
    if key == keyboard.Key.f11: # Start Listener
        running = True
        print("Started listening for key presses.")
        
    elif key == keyboard.Key.f12:
        running = False
        print("Stopped listening for key presses.")
        return False  # Stop listener

def on_click(x, y, button, pressed):
    if running and button == mouse.Button.left and pressed: # Keybind for screenshot
        print("Left mouse button clicked.")
        threading.Thread(target=take_screenshot).start()

# Start the keyboard listener
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Start the mouse listener
with mouse.Listener(on_click=on_click) as mouse_listener:
    mouse_listener.join()
