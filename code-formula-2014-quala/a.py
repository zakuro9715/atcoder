N = int(input())
for i in range(100):
    if i * i * i == N:
        print('YES')
        break
else:
    print('NO')
