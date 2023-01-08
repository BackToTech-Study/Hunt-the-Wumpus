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
  elif cave_number == 20:  # change this line
    return [cave_number - 1, cave_number - 3]

def test_get_caves_adjacent_to():
  assert get_caves_adjacent_to(1) == [2, 4]
  assert get_caves_adjacent_to(2) == [1, 3, 5]
  assert get_caves_adjacent_to(3) == [2, 6]
  assert get_caves_adjacent_to(4) == [1, 5, 7]
  assert get_caves_adjacent_to(5) == [2, 4, 6, 8]
  assert get_caves_adjacent_to(6) == [3, 5, 9]
  assert get_caves_adjacent_to(7) == [4, 8, 10]
  assert get_caves_adjacent_to(8) == [5, 7, 9, 11]
  assert get_caves_adjacent_to(9) == [6, 8, 12]
  assert get_caves_adjacent_to(10) == [7, 11, 13]
  assert get_caves_adjacent_to(11) == [8, 10, 12, 14]
  assert get_caves_adjacent_to(12) == [9, 11, 15]
  assert get_caves_adjacent_to(13) == [10, 14, 16]
  assert get_caves_adjacent_to(14) == [11, 13, 15, 17]
  assert get_caves_adjacent_to(15) == [12, 14, 18]
  assert get_caves_adjacent_to(16) == [13, 17, 19]
  assert get_caves_adjacent_to(17) == [14, 16, 18, 20]
  assert get_caves_adjacent_to(18) == [15, 17, 19]
  assert get_caves_adjacent_to(19) == [16, 18, 20]
  assert get_caves_adjacent_to(20) == [17, 19]

test_get_caves_adjacent_to()
