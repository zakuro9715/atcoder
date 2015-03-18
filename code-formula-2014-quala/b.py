input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
p = ['.' if v in A else ('o' if v in B else 'x') for v in range(10)]

print('{0} {1} {2} {3}'.format(p[7], p[8], p[9], p[0]))
print(' {0} {1} {2}'.format(p[4], p[5], p[6]))
print('  {0} {1}'.format(p[2], p[3]))
print('   {0}'.format(p[1]))
