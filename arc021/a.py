t = [input().split() + [0] for i in range(4)] + [[0] * 4]
print(t)
for y in range(0, 4):
  for x in range(0, 4):
    if t[y][x] == t[y + 1][x] or t[y][x] == t[y][x + 1]:
      print("CONTINUE")
      exit()
print("GAMEOVER")
