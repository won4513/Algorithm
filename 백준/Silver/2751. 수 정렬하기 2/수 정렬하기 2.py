#백준 2751
import sys

n = int(sys.stdin.readline())
x = []

for i in range(n):
  x.append(int(sys.stdin.readline()))
for i in sorted(x):
  print(i)

