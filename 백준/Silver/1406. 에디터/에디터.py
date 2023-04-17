from sys import stdin
from collections import deque


n = stdin.readline().rstrip()
t = int(stdin.readline()) 

a = deque() #커서 앞
b = deque() #커서 뒤

for i in n:
    a.append(i)

for i in range(t):
    now = stdin.readline().split()

    if now[0] == 'L':
        if len(a) != 0:
            b.appendleft(a.pop())
    elif now[0] == 'D':
        if len(b) != 0:
            a.append(b.popleft())
    elif now[0] == 'B':
        if len(a) != 0:
            a.pop()
        
    elif now[0] == 'P':
        a.append(now[1])

a = a + b

for now in a:
    print(now, end = '')   
    
        
           