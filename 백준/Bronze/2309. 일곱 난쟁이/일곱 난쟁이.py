1#백준 2309
k =[]
for i in range(9):
  a = int(input())
  k.append(a)
k.sort()

a = sum(k)
for i in range(len(k)):
  for j in range(i+1,len(k)):
    if a - k[i] - k[j] == 100:
      for _ in range(len(k)):
        if _ == i or _ ==  j:
          pass
        else:
          print(k[_])
      exit()

