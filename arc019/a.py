t = {'O': '0', 'D': '0', 'I': '1', 'Z': '2', 'S': '5', 'B': '8'}
print(''.join([t[c] if c in t else c for c in input()]))
