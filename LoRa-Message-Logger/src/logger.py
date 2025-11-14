from config import LOG_FILE
import datetime

def log_event(message):
    timestamp = datetime.datetime.now()
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")
