# config_manager.py
import requests

class ConfigManager:
    def __init__(self, config_url):
        self.config_url = config_url
        self.config = {
            "screenshot_interval": 300,
            "blur": False
        }

    def poll_for_updates(self):
        try:
            response = requests.get(self.config_url)
            if response.status_code == 200:
                self.config = response.json()
                print("Configuration updated: ", self.config)
        except Exception as e:
            print(f"Failed to fetch config: {str(e)}")
        return self.config
