import requests

def fetch_pokemon_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def extract_pokemon_info(data):
    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    return name, abilities

def main():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    data = fetch_pokemon_data(url)
    name, abilities = extract_pokemon_info(data)
    print(f"Name: {name}")
    print(f"Abilities: {abilities}")

if __name__ == "__main__":
    main()