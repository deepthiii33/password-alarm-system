# 🔐 Password Alarm System

A beginner-friendly Python security tool that monitors password attempts and triggers an alarm after 3 failed logins.

##  Features

- Accepts password input
- Allows 3 login attempts
- Triggers an audible alarm using `winsound` (Windows)
- Locks access for 60 seconds after 3 failed attempts
- Logs all attempts to a file

##  Files

- `password_alarm.py` — main Python script
- `alarm_log.txt` — auto-generated log file

##  How to Run

1. Clone the repo:
   ```bash
      git clone https://github.com/deepthiii33/password-alarm-system
      cd password-alarm-system
2. Download the zip file from code and extract , then open the python file
3. Run the script :
    ```bash
       python password_alarm.py

## Requirements
- Python 3.x
- Windows OS (uses winsound module)
