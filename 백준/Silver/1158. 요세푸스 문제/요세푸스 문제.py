#백준 1158

n, k = map(int, input().split())

x = []
now = 0
a = []
for i in range(1,n+1):
  x.append(i)

for i in range(n):
  now += k-1
  if now >= len(x):
    now = now % len(x)
  a.append(str(x.pop(now)))
  

print("<", ", ".join(a), ">", sep = '')




