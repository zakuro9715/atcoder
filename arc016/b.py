N = input()
ox = "........."
ans = 0
for i in range(N):
  x = raw_input()
  for j in range(9):
    if x[j] == 'x' or x[j] == 'o' and ox[j] != 'o':
      ans += 1
  ox = x
print ans
