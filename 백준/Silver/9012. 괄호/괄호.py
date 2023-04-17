#백준 9012

n = int(input())

for i in range(n):
  a = []
  b = []
  x = input()
  for j in x:
    if j == '(':
      a.append(j)
    else:
      b.append(j)
    if len(b) > len(a):
      break
      
  if len(a) == len(b):
    print('YES')
  else:
    print('NO')
  
  
