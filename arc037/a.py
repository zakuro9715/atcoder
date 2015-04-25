input()
print(sum([max(0, 80 - v) for v in map(int, input().split())]))
