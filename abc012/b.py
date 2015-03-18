N = int(input())
print("{0:02}:{1:02}:{2:02}".format(N // 3600, N % 3600 // 60, N % 60))
