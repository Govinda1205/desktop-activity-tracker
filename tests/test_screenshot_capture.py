import unittest
from screenshot_capture import ScreenshotCapture
import os

class TestScreenshotCapture(unittest.TestCase):
    def test_take_screenshot(self):
        capture = ScreenshotCapture(blur=False)
        file_path = capture.take_screenshot()
        self.assertTrue(os.path.exists(file_path))
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()
