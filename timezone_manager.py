# timezone_manager.py
from datetime import datetime
import time
import pytz

class TimeZoneManager:
    def __init__(self):
        self.current_timezone = pytz.timezone('UTC')

    def update_timezone(self):
        self.current_timezone = pytz.timezone(time.tzname[0])
        print(f"Timezone updated to {self.current_timezone}")

    def log_event(self, event):
        current_time = datetime.now(self.current_timezone)
        print(f"{event} at {current_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
