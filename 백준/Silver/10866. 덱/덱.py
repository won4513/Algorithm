#백준 10866
import sys
from collections import deque

n = int(sys.stdin.readline())
x = deque()

for i in range(n):
  a = sys.stdin.readline().split()
  order = a[0]

  if order == 'push_back':
    x.append(a[1])
  elif order == 'push_front':
    x.appendleft(a[1])
  elif order == 'pop_front':
    if len(x) == 0:
      print(-1)
    else:
      print(x[0])
      x.popleft()
  elif order == 'pop_back':
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
  elif order == 'front':
    if len(x) == 0:
      print(-1)
    else:
      print(x[0])
  elif order == 'back':
    if len(x) == 0:
      print(-1)
    else:
      print(x[-1])


