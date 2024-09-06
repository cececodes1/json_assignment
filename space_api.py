import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    try:
        response = requests.get(url)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    try:
        planets = response.json()['bodies']
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")
        return

    for planet in planets:
        if planet.get('isPlanet'):  
            try:
                name = planet['englishName']
                mass = planet['mass']['massValue']
                orbit_period = planet['perihelion']
                print(f"Name: {name}, Mass: {mass}, Perihelion: {orbit_period} AU")
            except (KeyError, TypeError) as e:
                print(f"Error: {e}")

fetch_planet_data()