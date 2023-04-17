#백준11726
n = int(input())
a,b = 1, 2
for i in range(2,n+1):
  a,b = b, a+b
print(a%10007)