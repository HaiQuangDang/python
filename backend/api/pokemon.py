import requests

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_data = {}
        pokemon_data["name"] = data["name"]
        pokemon_data["id"] = data["id"]
        pokemon_data["weight"] = data["weight"]
        pokemon_data["height"] = data["height"]
        return pokemon_data
    else:
        return(f"Failed to get pokemon info, status: {response.status_code}")


pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)
print(pokemon_info)
