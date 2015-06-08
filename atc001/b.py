N, Q = map(int, input().split())
s = [i for i in range(N)]

def root(a):
    if s[a] == a:
        return a
    else:
        s[a] = root(s[a])
        return s[a]

def unite(a, b):
    aa, bb = root(a), root(b)
    s[aa] = bb

def find(a, b):
    return root(a) == root(b)

for q in range(Q):
    p, a, b = map(int, input().split())
    if p:
        print('Yes' if find(a, b) else 'No')
    else:
        unite(a, b)
