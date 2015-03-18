A = list(input())
B = list(input())

x = []
ma, mb = [0] * 30, [0] * 30
for i in range(len(A)):
    if A[i] != B[i]:
        x.append(i)
    ma[ord(A[i]) - ord('a')] += 1
    mb[ord(B[i]) - ord('a')] += 1

same = False
for i in range(30):
    if ma[i] != mb[i]:
        print('NO')
        exit()
    if ma[i] > 1:
        same = True
if len(x) > 6:
    print('NO')
    exit()

if not x:
    print('YES' if same else 'NO')
    exit()

for v11 in x:
    for v12 in x:
        for v21 in x:
            for v22 in x:
                for v31 in x:
                    for v32 in x:
                        A[v11], A[v12] = A[v12], A[v11]
                        A[v21], A[v22] = A[v22], A[v21]
                        A[v31], A[v32] = A[v32], A[v31]
                         
                        n = 0
                        if v11 == v12:
                            n += 1
                        if v21 == v22:
                            n += 1
                        if v31 == v32:
                            n += 1
                        if not same and (n == 3 or n == 1):
                            continue
                        
                        if A == B:
                            print("YES")
                            exit()
                         
                        A[v11], A[v12] = A[v12], A[v11]
                        A[v21], A[v22] = A[v22], A[v21]
                        A[v31], A[v32] = A[v32], A[v31]
print("NO")
