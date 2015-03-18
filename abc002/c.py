p = map(float, raw_input().split())
l = [0.0] * 3
for i in range(len(p) / 2):
  l[i] = pow(pow(p[i * 2] - p[((i + 1) * 2 ) % 6], 2) + pow(p[i * 2 + 1] - p[((i + 1) * 2 + 1) % 6], 2), 0.5)
s = sum(l) / 2
print pow(s * (s - l[0]) * (s - l[1]) * (s - l[2]), 0.5)
