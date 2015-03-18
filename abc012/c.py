r = 2025 - int(input())
for i in range(1, 10):
    if(r % i or r // i > 9):
        continue
    print("{0} x {1}".format(i, r // i))
