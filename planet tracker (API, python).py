# ======================================================
# Space Labs – Solar System Planet Tracker
# Author: Petra Továrková
# Fetches planetary parameters from The Solar System OpenData API.
# ======================================================

import requests

def get_planet_data(planet_name):
    # API endpoint for solar system bodies
    url = f"https://api.le-systeme-solaire.net/rest/bodies/{planet_name.strip().lower()}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            # Print basic physical and orbital characteristics
            print(f"\n🪐 Planet: {data.get('englishName', 'N/A')}")
            
            # Safely handle potential missing mass attributes
            mass_info = data.get("mass")
            if mass_info:
                print(f"Mass: {mass_info.get('massValue')} x 10^{mass_info.get('massExponent')} kg")
            else:
                print("Mass: Data not available")

            print(f"Mean Radius: {data.get('meanRadius', 'N/A')} km")
            print(f"Surface Gravity: {data.get('gravity', 'N/A')} m/s²")
            print(f"Orbital Period: {data.get('sideralOrbit', 'N/A')} days")
            
            print("\nSpace fact loaded successfully! Keep reaching for the stars! 🪐✨")
        else:
            print("❌ Planet not found! Please check the spelling and try again.")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    planet = input("Enter planet name (e.g., Mars, Jupiter, Earth): ")
    get_planet_data(planet)
