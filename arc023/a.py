y, m, d = int(input()), int(input()), int(input())
if m < 3:
  m += 12
  y -= 1
print(735369 - (365 * y + y // 4 - y // 100 + y // 400 + 306 * (m + 1) // 10 + d - 429))
