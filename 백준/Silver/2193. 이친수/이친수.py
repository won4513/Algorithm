#백준2193
n = int(input())
a,b = 1, 1
for i in range(2,n+1):
  a,b = b, a+b
print(a)