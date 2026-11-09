# ======================================================
# Space Labs – Moon Phase Calculator
# Author: Petra Továrková 
# Simple script to approximate the current moon phase.
# ======================================================

from datetime import datetime

def get_moon_phase(date):
    # Calculate the number of days since a known new moon baseline
    new_moon_date = datetime(2001, 1, 24, 13, 7)
    delta = date - new_moon_date
    days_since_new_moon = delta.total_seconds() / 86400.0
    
    # Average synodic month duration (lunar cycle length)
    moon_cycle_length = 29.53059
    phase = (days_since_new_moon % moon_cycle_length) / moon_cycle_length

    # Standard astronomical moon phase intervals
    if phase < 0.03 or phase >= 0.97:
        return "New Moon 🌑"
    elif phase < 0.22:
        return "Waxing Crescent 🌒"
    elif phase < 0.28:
        return "First Quarter 🌓"
    elif phase < 0.47:
        return "Waxing Gibbous 🌔"
    elif phase < 0.53:
        return "Full Moon 🌕"
    elif phase < 0.72:
        return "Waning Gibbous 🌖"
    elif phase < 0.78:
        return "Last Quarter 🌗"
    else:
        return "Waning Crescent 🌘"

# Get current date and print the result
today = datetime.now()
moon_phase = get_moon_phase(today)

print(f"Today's date: {today.strftime('%Y-%m-%d')}")
print(f"Current Moon Phase: {moon_phase}")
print("Remember to align your goals with the lunar energy today! 💫✨")
