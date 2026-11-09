# ======================================================
# Space Labs – Solar System Planet Tracker
# Author: Petra Továrková
# Live planetary data tracking with reliable offline fallback.
# (Because Pluto will ALWAYS be a planet in our hearts! 🪐)
# ======================================================

import requests

# Local astronomical fallback dataset (ensures 100% uptime without mandatory API keys)
LOCAL_PLANET_DATA = {
    "mercury": {"name": "Mercury", "mass": "3.3011 x 10^23", "radius": 2439.7, "gravity": 3.7, "orbit": 87.97},
    "venus": {"name": "Venus", "mass": "4.8675 x 10^24", "radius": 6051.8, "gravity": 8.87, "orbit": 224.7},
    "earth": {"name": "Earth", "mass": "5.9722 x 10^24", "radius": 6371.0, "gravity": 9.807, "orbit": 365.25},
    "mars": {"name": "Mars", "mass": "6.4171 x 10^23", "radius": 3389.5, "gravity": 3.721, "orbit": 686.98},
    "jupiter": {"name": "Jupiter", "mass": "1.8982 x 10^27", "radius": 69911, "gravity": 24.79, "orbit": 4332.59},
    "saturn": {"name": "Saturn", "mass": "5.6834 x 10^26", "radius": 58232, "gravity": 10.44, "orbit": 10759.22},
    "uranus": {"name": "Uranus", "mass": "8.6810 x 10^25", "radius": 25362, "gravity": 8.69, "orbit": 30685.4},
    "neptune": {"name": "Neptune", "mass": "1.0241 x 10^26", "radius": 24622, "gravity": 11.15, "orbit": 60189.0},
    "pluto": {"name": "Pluto", "mass": "1.3030 x 10^22", "radius": 1188.3, "gravity": 0.62, "orbit": 90560.0}
}

def get_planet_data(planet_name):
    clean_input = planet_name.strip().lower()

    # Mapping English planet names to API IDs
    body_ids = {
        "earth": "terre", "moon": "lune", "sun": "soleil",
        "mercury": "mercure", "venus": "venus", "mars": "mars",
        "jupiter": "jupiter", "saturn": "saturne", "uranus": "uranus",
        "neptune": "neptune", "pluto": "pluton"
    }

    target_id = body_ids.get(clean_input, clean_input)
    url = f"https://api.le-systeme-solaire.net/rest/bodies/{target_id}"

    # Try live API request first
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            display_name = data.get("englishName", clean_input.capitalize())
            is_pluto = clean_input == "pluto" or target_id == "pluton"

            print(f"\n🌐")
            if is_pluto:
                print(f"🪐 Planet: {display_name} (Official Status: 100% Real Planet in this lab! ✨)")
            else:
                print(f"🪐 Planet: {display_name}")

            mass_info = data.get("mass")
            if mass_info and isinstance(mass_info, dict):
                print(f"Mass: {mass_info.get('massValue')} x 10^{mass_info.get('massExponent')} kg")
            else:
                print("Mass: Data not available")

            print(f"Mean Radius: {data.get('meanRadius', 'N/A')} km")
            print(f"Surface Gravity: {data.get('gravity', 'N/A')} m/s²")
            print(f"Orbital Period: {data.get('sideralOrbit', 'N/A')} days")
            
            if is_pluto:
                print("\nPluto data loaded via API! Never let anyone tell you you're too small to be a planet. 💖✨")
            else:
                print("\nSpace fact loaded successfully! Keep reaching for the stars! 🪐✨")
            return
    except requests.exceptions.RequestException:
        pass  # Fallback to local database seamlessly

    # Fallback execution if API is auth-restricted or offline
    if clean_input in LOCAL_PLANET_DATA:
        data = LOCAL_PLANET_DATA[clean_input]
        display_name = data["name"]
        is_pluto = clean_input == "pluto"

        print(f"\n📡")
        if is_pluto:
            print(f"Planet: {display_name} (Always a Planet in this lab! ✨)")
        else:
            print(f"Planet: {display_name}")

        print(f"Mass: {data['mass']} kg")
        print(f"Mean Radius: {data['radius']} km")
        print(f"Surface Gravity: {data['gravity']} m/s²")
        print(f"Orbital Period: {data['orbit']} days")

        if is_pluto:
            print("\nPluto data loaded! Never let anyone tell you you're too small to be a planet. 💖✨")
        else:
            print("\nSpace fact loaded successfully! Keep reaching for the stars! 🪐✨")
    else:
        print("❌ Planet not found! Please check the spelling (e.g., Earth, Mars, Jupiter, Pluto).")

if __name__ == "__main__":
    planet = input("Enter planet name (e.g., Mars, Jupiter, Earth, Pluto): ")
    get_planet_data(planet)