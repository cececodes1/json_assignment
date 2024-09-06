import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    planet_list = []

    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit_period = planet.get('sideralOrbitalPeriod', 'Unknown')
            planet_list.append((name, mass, orbit_period))

            print("Planet:", name)
            print("Mass:", mass)
            print("Orbit Period:", orbit_period)
            print("------------------------")
    
    return planet_list  # You need to return the planet_list

def find_heaviest_planet(planets):
    heaviest_planet = planets[0]
    for planet in planets:
        if planet[1] > heaviest_planet[1]:
            heaviest_planet = planet
    print("The heaviest planet is", heaviest_planet[0], "with a mass of", heaviest_planet[1], "Earth masses")
    return heaviest_planet  # You need to return the heaviest planet

def find_longest_orbit_planet(planets):
    longest_orbit_planet = planets[0]
    for planet in planets:
        if planet[2] > longest_orbit_planet[2]:
            longest_orbit_planet = planet
    print("The planet with the longest orbit is", longest_orbit_planet[0], "with an orbit period of", longest_orbit_planet[2], "days")
    return longest_orbit_planet  # You need to return the longest orbit planet


planets = fetch_planet_data()
heaviest_planet = find_heaviest_planet(planets)
longest_orbit_planet = find_longest_orbit_planet(planets)

print("Planetary Information:")
for planet in planets:
    print(f"Planet: {planet[0]}, Mass: {planet[1]}, Orbit Period: {planet[2]} days")
    print("--------------------")

print(f"The heaviest planet is {heaviest_planet[0]} with a mass of {heaviest_planet[1]} kg.")
print(f"The planet with the longest orbit period is {longest_orbit_planet[0]} with an orbit period of {longest_orbit_planet[2]} days.")