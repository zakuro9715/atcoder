print('YES' if input().replace('ch', 'k').translate(str.maketrans('oku', '000')).isdigit() else 'NO') 
