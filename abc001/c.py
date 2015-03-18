p = [2, 15, 33, 54, 79, 107, 138, 171, 207, 244, 284, 326]
d = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
deg, dis = map(int, raw_input().split())

for i in range(len(p)):
  if int(dis * 10 / 60.0 + 0.5) <= p[i]:
    dis = i
    break
else:
  dis = len(p)  
for i in range(len(d)):
  if deg * 10 < 1125 + 36000 / 16.0 * (i):
    deg = d[i]
    break
else:
  deg = "N"

if dis == 0:
  deg = "C"
print deg, dis
