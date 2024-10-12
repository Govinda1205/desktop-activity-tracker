# screenshot_capture.py
import pyautogui
from PIL import Image, ImageFilter
import time

class ScreenshotCapture:
    def __init__(self, capture_interval=300, blur=False):
        self.capture_interval = capture_interval
        self.blur = blur
        self.screenshot_counter = 0

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        if self.blur:
            screenshot = screenshot.filter(ImageFilter.GaussianBlur(5))
        file_path = f"screenshot_{self.screenshot_counter}.png"
        screenshot.save(file_path)
        self.screenshot_counter += 1
        return file_path

    def start_capture(self):
        while True:
            file_path = self.take_screenshot()
            print(f"Screenshot saved: {file_path}")
            time.sleep(self.capture_interval)
