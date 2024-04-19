def extract_pokemon_data(pokemon_data):

    ext_data = {
        "name": pokemon_data["name"],
        "height": pokemon_data["height"],
        "weight": pokemon_data["weight"],
        "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
        "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]]
    }
    return ext_data