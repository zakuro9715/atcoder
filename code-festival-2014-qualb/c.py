S1, S2, S3 = input(), input(), input()
N = len(S1)
M1, M2 = [0] * 30, [0] * 30
O1, O2 = 0, 0
for i in S3:
    M1[ord(i) - ord('A')] += 1
    M2[ord(i) - ord('A')] += 1

for i in S1:
    n = ord(i) - ord('A')
    if M1[n] > 0:
        O1 += 1
        M1[n] -= 1

for i in S2:
    n = ord(i) - ord('A')
    if M2[n] > 0:
        O2 += 1
        M2[n] -= 1

if O1 < N / 2 or O2 < N / 2:
    print('NO')
else:
    print('YES')
