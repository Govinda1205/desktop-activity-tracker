# Desktop Activity Tracker

## Project Overview
A Python-based desktop agent that tracks employee activity, captures screenshots, and uploads data to Amazon S3.

## Requirements
- Python 3.7+
- AWS CLI
- Third-party Libraries:
  - boto3:To handle file uploads to Amazon S3
  - pytz:To handle timezone changes
  - pillow:equired for image manipulation and applying blur effects
  - pynput(for activity tracking):To monitor user activity (mouse/keyboard input)
  - pyautogui:For taking screenshots
  - request:To handle HTTP requests for fetching configuration data
  - pytest:To write and run unit tests

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
2.Install dependencies:
  pip install -r requirements.txt
3.Configure AWS credentials:
  aws configure
4.Run the application:
  python agent.py
5.Optional Features
  Screenshot blurring
  Time zone adjustment

