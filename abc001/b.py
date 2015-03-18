M = input()
if M < 100:
  print "00"
elif M <= 5000:
  print "%02d" % (M / 100)
elif M <= 30000:
  print M / 1000 + 50
elif M <= 70000:
  print (M / 1000 - 30) / 5 + 80
else:
  print 89
