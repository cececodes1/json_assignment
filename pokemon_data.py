import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    return data

def extract_pokemon_info(data):
    name = data ['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    weight = data['weight']
    return name, abilities, weight

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight += pokemon[2]
    average_weight = total_weight / len(pokemon_list)
    return average_weight

def main():
    pokemon_names = ["pikachu", "bulbasaur", "charmander"]
    pokemon_list = []
    for pokemon_name in pokemon_names:
        data = fetch_pokemon_data(pokemon_name)
        name, abilities, weight = extract_pokemon_info(data)
        pokemon_list.append((name, abilities, weight))

    average_weight = calculate_average_weight(pokemon_list)

    print("Pokemin Info:")
    for pokemon in pokemon_list:
        print(f"Name: {pokemon[0]}")
        print(f"Abilities: {pokemon[1]}")
        print(f"Weight: {pokemon[2]}")
        print()
    
    print(f"Average Weight: {average_weight}")

if __name__ == "__main__":
    main()