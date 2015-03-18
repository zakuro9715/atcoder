s = input()
if len(s) == 1:
  print(0)
  exit()

not_symmetry_count = 0
for i in range(len(s) // 2):
  if s[i] != s[-i - 1]:
    not_symmetry_count += 1

if not_symmetry_count == 0 and len(s) % 2 == 1:
  print(25 * (len(s) - 1))
elif not_symmetry_count != 1:
  print(25 * len(s))
else:
  print(25 * len(s) - 2)
