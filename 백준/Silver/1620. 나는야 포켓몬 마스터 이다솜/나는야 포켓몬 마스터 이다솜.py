#백준1620
import sys
n, m = map(int, sys.stdin.readline().split())
num = {}
name = {}
for i in range(1,n+1):
  p = sys.stdin.readline().rstrip()
  num[i] = p
  name[p] = i

for i in range(m):
  x = sys.stdin.readline().rstrip()
  if x.isdigit() == True:
    print(num[int(x)])
  else:
    print(name[x])