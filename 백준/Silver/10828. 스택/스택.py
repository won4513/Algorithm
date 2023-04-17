#백준 10828
import sys

n = int(sys.stdin.readline())
x = []

for i in range(n):
  a = sys.stdin.readline().split()
  order = a[0]

  if order == 'push':
    x.append(a[1])
  elif order == 'pop':
    if len(x) == 0:
      print(-1)
    else:
      print(x[-1])
      x.pop()
  elif order == 'size':
    print(len(x))
  elif order == 'empty':
    if len(x) == 0:
      print(1)
    else:
      print(0)
  elif order == 'top':
    if len(x) == 0:
      print(-1)
    else:
      print(x[-1])


