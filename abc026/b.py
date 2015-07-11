print(sum(map(lambda v: v[1] * (-1)**v[0], enumerate(reversed(sorted([int(input())**2 * 3.14159265358979 for i in range(int(input()))]))))))
