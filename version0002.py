import random

def draw_cave(cave_numbers, wumpus_location, player_location, visited_caves):
  """Draw the current state of the cave, with X's marking the player's location and W's marking the wumpus's location."""
  for index, cave in enumerate(cave_numbers):
    if index + 1 in visited_caves:
      print("  ", end="")
    elif cave == wumpus_location:
      print("W ", end="")
    elif cave == player_location:
      print("X ", end="")
    else:
      print("  ", end="")
  print()

def get_caves_adjacent_to(cave_number):
  """Get the cave numbers adjacent to the given cave."""
  if cave_number in [1, 2, 3]:
    return [cave_number + 1, cave_number + 3]
  elif cave_number in [4, 7, 10, 13, 16, 19]:
    return [cave_number - 1, cave_number + 1, cave_number + 3]
  elif cave_number in [5, 8, 11, 14, 17, 20]:
    return [cave_number - 1, cave_number + 3]
  elif cave_number in [6, 9, 12, 15, 18]:
    return [cave_number - 3, cave_number + 1]
  elif cave_number == 20:
    return [cave_number - 1, cave_number - 3]

def get_hints(cave_numbers, wumpus_location, player_location):
  """Get hints about the location of the Wumpus based on the player's location and the locations of the adjacent caves."""
  hints = []
  for cave in get_caves_adjacent_to(player_location):
    if cave == wumpus_location:
      hints.append("I smell a wumpus!")
    elif cave in get_caves_adjacent_to(wumpus_location):
      hints.append("I feel a draft.")
  return hints

def ask_for_cave(cave_numbers, player_location):
  """Ask the player to choose a cave to move to, and return the cave number they choose."""
  print("Which cave would you like to move to? (1-20)")
  while True:
    user_input = input()
    if not user_input.isdigit():
      print("That's not a number! Please enter a number between 1 and 20.")
      continue
    cave_number = int(user_input)
    if cave_number not in cave_numbers:
      print("That's not a valid cave number! Please enter a number between 1 and 20.")
      continue
    if cave_number in get_caves_adjacent_to(player_location):
      return cave_number
    else:
      print("You can't get there from here! Please enter a cave number adjacent to your current location.")

def play():
  print("Welcome to Hunt the Wumpus!")
  cave_numbers = range(1, 21)
