#백준 10992
n = int(input())

if n == 1:
  print('*')
else:
  print((n-1)*' ' + '*')
  for i in range(2, n):
    print((n-i)*' ' + '*' + (2*i-3) * ' ' + '*')
  print((2*n-1)*'*')

