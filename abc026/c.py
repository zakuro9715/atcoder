N = int(input())
B = [-1] + [int(input()) - 1 for i in range(N - 1)]
s = [[0, 0] for i in range(N)]


def get_queue():
    enqueue = [B[i] > -1 for i in range(N)]
    for b in B:
        if b > -1:
            enqueue[b] = False
    return list(filter(lambda x: enqueue[x], range(N)))

while True:
    qu = get_queue()
    if len(qu) == 0:
        break
    for q in qu:
        b = B[q]
        if type(s[q]) == list:
            s[q] = sum(s[q]) + 1
            B[q] = -1
        if not s[b][0] or s[b][0] > s[q]:
            s[b][0] = s[q]
        s[b][1] = max(s[b][1], s[q])
print(sum(s[0]) + 1)
