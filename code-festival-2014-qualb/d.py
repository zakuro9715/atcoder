class T:
    def __init__(self, n, h, l=None, r=None):
        self.n = n
        self.h = h
        self.l = l
        self.r = r
    def dfs(self, i, vec):
        global A
        print('start', self.n)
        print('i', i)

        rx = len(vec) - 1
        lx = 0
        target = self
        fa, fb = False, False
        while True:
            print('vec ', [v.n for v in vec])
            if not fa:
                if target.n >= len(vec):
                    A[target.n] += len(vec) - target.n
                    fa = True
                for j in range(i + 1, len(vec)):
                    if vec[i].h < vec[j].h:
                        rx = vec[i].n
                        print('rx', rx)
                        break
                else:
                    print('r ', rx)
                    A[target.n] += rx - target.n
                    fa = True

            if not fb:
                if 
                for j in range(i - 1, -1, -1):
                    if vec[i].h < vec[j].h:
                        print('lx', lx)
                        lx = vec[i].n
                        break
                else:
                    print('l ', lx)
                    A[target.n] += target.n - lx
                    fb = True
            if fa and fb:
                break
            if not (target.l or target.r):
                break
            tl = target.l if target.l else None
            tr = target.r if target.r else None
            target = T(target.n, target.h, tl[-1].r if tl else None, tr[0].l if tr else None)
            vec = (tl if tl else []) + [target] + (tr if tr else [])
            print('next')
            print()

        print('end', self.n)
        print('A', A[self.n])
        print()
        if self.l:
            for i, t in enumerate(self.l):
                t.dfs(i, self.l)
        if self.r:
            for i, t in enumerate(self.r):
                t.dfs(i, self.r)

N = int(input())
H = [T(i, int(input()))  for i in range(N)]
A = [0] * N

while True:
    l = []
    b = -1

    
    for i, v, in enumerate(H):
        if i == 0 or i == N - 1:
            if i == 0 and H[0].h > H[1].h:
                l.append(T(i, H[0].h))
            elif i == N - 1 and H[-1].h > H[-2].h:
                l.append(T(i, H[-1].h, H[b + 1:-1]))
        
        elif H[i].h > H[i - 1].h and H[i].h > H[i + 1].h:
            v = H[b + 1: i]
            if l:
                l[-1].r = v
            l.append(T(i, H[i].h, v))
    if l:
        H = l
    if len(l) <= 1:
        break

for i, t in enumerate(H):
    t.dfs(i, H)

print(A)
