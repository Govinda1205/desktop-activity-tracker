# activity_tracker.py
import pynput
import threading
import random

class ActivityTracker:
    def __init__(self):
        self.mouse_controller = pynput.mouse.Controller()
        self.keyboard_controller = pynput.keyboard.Controller()
        self.mouse_activity = False
        self.keyboard_activity = False
        self.lock = threading.Lock()

    def on_move(self, x, y):
        with self.lock:
            self.mouse_activity = True

    def on_click(self, x, y, button, pressed):
        with self.lock:
            self.mouse_activity = True

    def on_scroll(self, x, y, dx, dy):
        with self.lock:
            self.mouse_activity = True

    def on_key_press(self, key):
        with self.lock:
            self.keyboard_activity = True

    def start_monitoring(self):
        mouse_listener = pynput.mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll)
        keyboard_listener = pynput.keyboard.Listener(
            on_press=self.on_key_press)

        mouse_listener.start()
        keyboard_listener.start()

    def detect_scripted_activity(self):
        # Detect irregularities in user activity (simplified)
        return random.choice([True, False])

    def get_activity(self):
        with self.lock:
            activity = self.mouse_activity or self.keyboard_activity
            self.mouse_activity = False
            self.keyboard_activity = False
        return activity
