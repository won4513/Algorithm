#백준 11652


n = int(input())
a = {}

for i in range(n):
  x = int(input())
  if x in a:
    a[x] += 1
  else:
    a[x] = 1

a = sorted(a.items(), key = lambda x: (-x[1],x[0]))
print(a[0][0])