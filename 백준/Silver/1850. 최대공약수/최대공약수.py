#백준 1850
import math
A, B = map(int, input().split())

k = math.gcd(A,B)

print('1'* k)

