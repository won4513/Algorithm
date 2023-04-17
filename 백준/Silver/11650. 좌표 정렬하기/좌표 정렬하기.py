#백준 11650

import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
  a.append(list(map(int, input().split())))

a.sort()
for i in a:
  print(i[0], i[1])