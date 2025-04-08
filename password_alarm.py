import time
from datetime import datetime
import winsound  #  For alarm sound on Windows

# Configuration
correct_password = "deepthi123"
max_attempts = 3
log_file = "alarm_log.txt"

def log_attempt(status, entered_pass):
    with open(log_file, "a") as f:
        f.write(f"[{datetime.now()}] Attempt: '{entered_pass}' -> {status}\n")

def trigger_alarm():
    print("\n🚨 ALARM TRIGGERED: 3 Failed Login Attempts!")
    print("System is temporarily locked for 1 minute...")

    #  Beep alarm: 3 times
    for i in range(3):
        winsound.Beep(1000, 600)  # frequency (Hz), duration (ms)
        time.sleep(0.3)

    #  Log the alarm
    with open(log_file, "a") as f:
        f.write(f"[{datetime.now()}] >>> ALARM TRIGGERED <<<\n")

    #  Lockout countdown
    for remaining in range(60, 0, -1):
        print(f"⏳ Locked: {remaining} seconds remaining...", end="\r")
        time.sleep(1)

    print("\n🔓 System unlocked. You may try again.")

def main():
    attempts = 0
    print("🔐 Secure Access Portal\n")

    while attempts < max_attempts:
        try:
            password = input("Enter your password: ")  #  Shows what you type
        except Exception as e:
            print(f"Error reading input: {e}")
            continue

        if password == correct_password:
            print("✅ Access granted.")
            log_attempt("SUCCESS", password)
            break
        else:
            attempts += 1
            print(f"❌ Incorrect password. Attempts left: {max_attempts - attempts}")
            log_attempt("FAIL", password)

    if attempts == max_attempts:
        trigger_alarm()

if __name__ == "__main__":
    main()
