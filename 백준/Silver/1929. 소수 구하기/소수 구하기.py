#백준 1929
import math

m,n = map(int, input().split())
def is_prime_num(x):
  if x == 1:
      return False
  for j in range(2,int(math.sqrt(x))+1):
      if x % j == 0:
        return False
  return True

for i in range(m, n+1):
  if is_prime_num(i) == True:
    print(i)


      
