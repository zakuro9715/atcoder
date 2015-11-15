sq = [i**2 for i in range(1, 1000)]
n = int(input())
for s in sq:
    if n <= s:
        print(s - n)
        exit()
