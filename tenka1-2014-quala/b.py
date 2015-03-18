class Event(object):
    def __init__(self, back=0, act=True, t=0, hit=0):
        self.back = back
        self.act = act
        self.throw= t
        self.hit = hit

def damage(v):
    return (int)(v * (1 + combo // 10 * 0.1))

def N(i):
    global kabu, events
    if not kabu:
        return
    kabu -= 1
    events[i + 7].back = 1
    events[i + 1].throw = 10
    events[i + 2].hit = 1

def C(i):
    global kabu, events
    if kabu < 3:
        return
    kabu -= 3
    events[i + 9].back = 3
    events[i + 3].throw = 50
    events[i + 4].hit = 1
    events[i + 1].act = events[i + 2].act = False

S = input()
n = len(S)
events = [Event() for i in range(n + 10)]
combo = 0
kabu = 5
d = 0
for i in range(n + 10):
    kabu += events[i].back
    d += damage(events[i].throw)
    combo += events[i].hit

    if i >= n or not events[i].act or S[i] == '-':
        continue
    if S[i] == 'N':
        N(i)
    if S[i] == 'C':
        C(i)
print(d)
