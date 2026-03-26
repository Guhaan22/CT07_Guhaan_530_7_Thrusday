# import random
# numbers = []
# for count in range(100):
#     generate = random.randint(1, 1000)
#     # check for no duplicates
#     while generate in numbers:
#         generate = random.randint(1, 1000)

#     numbers.append(generate)

# print(numbers)
import random
pokemons = [ "Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax", "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp", "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther", "Electabuzz" ]
powers = [ 55, 84, 49, 48, 45, 45, 52, 55, 110, 110, 85, 65, 134, 130, 110, 50, 125, 65, 110, 83 ]
# Find who is the most powerful pokemon in the lists
# 1. Find the max value in powers
powerful = max(powers)
print(powerful)
powerful_position = powers.index(powerful)

print(pokemons[powerful_position])







# pickOneCard = random.choice(pokemons)
# indexOfPickcard = pokemons.index(pickOneCard)
# firepower = powers[indexOfPickcard]
# print(pickOneCard, "has a fire power of", firepower)