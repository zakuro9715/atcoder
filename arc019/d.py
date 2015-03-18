for y in range(150):
  for x in range(150):
    if x == 0:
      print('.' if y % 2 == 0 else 0, end = "\n" if x == 149 else "")
    elif x == 149:
      print('.' if y % 2 == 1 else 0, end = "\n" if x == 149 else "")
    elif y == 0:
      print('.' if x % 2 == 1 else 0, end = "\n" if x == 149 else "")
    elif y == 149:
      print('.' if x % 2 == 0 else 0, end = "\n" if x == 149 else "")
    else:
      print('.', end = "")
