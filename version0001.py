import random

cave_numbers = range(1, 21)
wumpus_location = random.choice(cave_numbers)
player_location = random.choice(cave_numbers)
while player_location == wumpus_location:
    player_location = random.choice(cave_numbers)

print("Welcome to Hunt the Wumpus!")
print("You are in cave {}".format(player_location))

while True:
    print("Which cave do you want to move to? (1-20)")
    user_input = input()
    if not user_input.isdigit():
        print("That's not a number!")
        continue

    cave_number = int(user_input)
    if cave_number not in cave_numbers:
        print("That's not a valid cave number!")
        continue

    player_location = cave_number
    if player_location == wumpus_location:
        print("Aargh! You got eaten by the Wumpus!")
        break
    else:
        print("You are now in cave {}".format(player_location))
