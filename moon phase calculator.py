import math
from datetime import datetime

def get_moon_phase(date):
    # Calculate the number of days since the last new moon
    new_moon_date = datetime(2001, 1, 24)  # Example new moon date
    delta = date - new_moon_date
    days_since_new_moon = delta.days
    
    # The length of the lunar cycle (synodic month) is about 29.53 days
    moon_cycle_length = 29.53
    phase = (days_since_new_moon % moon_cycle_length) / moon_cycle_length

    # Moon phase interpretation
    if 0 <= phase < 0.03 or 0.97 <= phase < 1:
        return "New Moon"
    elif 0.03 <= phase < 0.23:
        return "First Quarter"
    elif 0.23 <= phase < 0.53:
        return "Full Moon"
    elif 0.53 <= phase < 0.73:
        return "Last Quarter"
    else:
        return "Waning Crescent"

# Get current date and calculate moon phase
today = datetime.today()
moon_phase = get_moon_phase(today)
print(f"Today's date: {today.strftime('%Y-%m-%d')}")
print(f"Current Moon Phase: {moon_phase}")
