print(['Draw' if a == b else 'Ant' if a < b else 'Bug' for a, b in [(abs(int(i)) for i in input().split())]][0])
