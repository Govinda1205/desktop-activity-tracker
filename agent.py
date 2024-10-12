# agent.py
import threading
import time
from activity_tracker import ActivityTracker
from screenshot_capture import ScreenshotCapture
from s3_uploader import S3Uploader
from config_manager import ConfigManager
#from timezone_manager import TimeZoneManager

class DesktopAgent:
    def __init__(self):
        self.activity_tracker = ActivityTracker()
        self.screenshot_capture = ScreenshotCapture()
        self.s3_uploader = S3Uploader(bucket_name='my-s3-bucket')
        self.config_manager = ConfigManager(config_url="https://example.com/config")
        #self.timezone_manager = TimeZoneManager()
        self.running = True

    def run(self):
        # Start activity tracker in the background
        self.activity_tracker.start_monitoring()

        # Start configuration polling in a separate thread
        config_thread = threading.Thread(target=self.poll_for_config_changes)
        config_thread.start()

        while self.running:
            # Detect and handle time zone changes
            #self.timezone_manager.update_timezone()

            # Capture and upload screenshots if there's genuine activity
            if self.activity_tracker.get_activity():
                if not self.activity_tracker.detect_scripted_activity():
                    screenshot_path = self.screenshot_capture.take_screenshot()
                    self.s3_uploader.upload_file(screenshot_path)
            time.sleep(60)  # Check every minute

    def poll_for_config_changes(self):
        while self.running:
            config = self.config_manager.poll_for_updates()
            self.screenshot_capture.capture_interval = config.get("screenshot_interval", 300)
            self.screenshot_capture.blur = config.get("blur", False)
            time.sleep(60)

    def stop(self):
        self.running = False

if __name__ == "__main__":
    agent = DesktopAgent()
    try:
        agent.run()
    except KeyboardInterrupt:
        agent.stop()
