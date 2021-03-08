#@Time:3/2/20211:52 PM
#@Author: Mini(Wang Han)
#@Site:
#@File:queue.py
#方法一
import queue

q = queue.SimpleQueue()

for _i in range(1, 42):
    q.put(_i)

i = 1
while q.qsize() > 2:
    if i % 3 == 0:
        q.get()
    else:
        q.put(q.get())
    i=i+1
print(q.get(),q.get())
#方法二
from collections import deque
q=deque([])
for i in range(1,42):
    q.append(i)
j=1
while len(q)>2:
    if j%3==0:
       q.popleft()
    else:
        q.append(q.popleft())
    j += 1
print(q)

