mem = [0] * 2401
N = input()
for i in range(N):
  st, en = map(int, raw_input().split('-'))
  st -= st % 5
  en += 5 - en % 5 if en % 5 else 0  
  if en % 100 == 60:
    en += 100 - 60
  mem[st] += 1
  mem[en] -= 1

m = 0
for i, v in enumerate(mem):
  if not m and mem[i] > 0:
    st = i
  if m and m + mem[i] <= 0:
    print "%04d-%04d" % (st, i)
  m += v
