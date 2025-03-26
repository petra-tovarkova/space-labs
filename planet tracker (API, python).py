#planet tracker (API, python)

#jakoze SPICE DATA no nee

import requests

def get_planet_data(planet_name):
    url = f"https://api.le-systeme-solaire.net/rest/bodies/{planet_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Planet: {data['englishName']}")
        print(f"Mass: {data['mass']['massValue']} x 10^{data['mass']['massExponent']} kg")
        print(f"Radius: {data['meanRadius']} km")
        print(f"Gravity: {data['gravity']} m/s²")
        print(f"Orbital Period: {data['sideralOrbit']} days")
    else:
        print("Planet not found!")

if __name__ == "__main__":
    planet = input("Enter planet name: ")
    get_planet_data(planet)
