from itertools import combinations
n,k=map(int,input().split())
l=list(combinations(str(n),k))
q=[]
for i in l:
  a=''.join(i)
  q.append(a)
print(min(q))
