import game
import itertools
import math
from common import *

class Mario(object):
    def __init__(self, text, score):
        self.text = text
        self.score = score

    def __unicode__(self):
        return 'Mario(text={0}, score={1})'.format(self.text, self.score)
    
    def __str__(self):
        return self.__unicode__()
    
    def __lt__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.text == other.text

    def cross(self, other):
        x1 = random.randrange(1, len(self.text) / 2)
        x2 = random.randrange(x1 + 1, len(self.text) - 2)
        re = random.randrange(0, 2)
        return Mario(self.text[:x1] + other.text[x1:x2] + self.text[x2:], 0)

heni = 8#%
heni_n = 20
tops_n = 20
mario_n = 40
savefile = 'mario.log'
f = open(savefile)

mario = [Mario(l.replace('\n', ''), 0) for l in f.readlines()]
mario += [Mario(create_rand_str(), 0) for i in range(mario_n)]
mario = mario[:mario_n]


for y in itertools.count():
    print('--------------第{0}世代--------------'.format(y))
    mario_next = []
    for m in mario:
        url, res, err = game.submit(m.text)
        m.score = int(res)
        print(m)
        wait_for_sec()

    mario.sort(reverse=True)
    tops = mario[:tops_n]
    for ma, mb in itertools.permutations(tops, 2):
        if ma == mb:
            continue
        mn = ma.cross(mb)
        if mn in mario:
            continue
        mario_next.append(mn)
    mario = mario_next[:mario_n]
    for m in mario:
        if random.randrange(0, 100) < heni:
            s = list(m.text)
            ss = create_rand_str(heni_n)
            begin = random.randrange(0, len(m.text) - heni_n)
            for i in range(begin, heni_n):
                s[i] = ss[i - begin]
            m.text = ''.join(s)

    f = open(savefile, 'w')
    for m in mario:
        f.writelines((m.text, '\n'))
    f.close()
