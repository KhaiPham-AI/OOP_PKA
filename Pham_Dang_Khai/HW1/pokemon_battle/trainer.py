from pokemon import Pokemon

class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        pokemon_details = pokemon.pokemon_details()
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon_details}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        pokemons_data = []
        for pokemon in self.pokemons:
            pokemons_data.append(pokemon.pokemon_details())
        pokemons_data = "\n- ".join(pokemons_data)
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n- {pokemons_data}"
