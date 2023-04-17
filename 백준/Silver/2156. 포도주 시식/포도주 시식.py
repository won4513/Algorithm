#백준2156
n = int(input())
x = []
for i in range(n):
  x.append(int(input()))

dp = [0]*n
dp[0] = x[0]
if n > 1:
  dp[1] = x[0] + x[1]
if n > 2:
  dp[2] = max(x[2] + x[0], x[2] + x[1], dp[1])
for i in range(3, n):
  dp[i] = max(dp[i-1],dp[i-3] + x[i-1] + x[i], dp[i-2] + x[i])

print(dp[n-1]) 



