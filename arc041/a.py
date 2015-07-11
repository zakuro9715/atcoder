x, y = map(int, input().split())
k = int(input())
print(x + k if y > k else x + y - (k - y))
