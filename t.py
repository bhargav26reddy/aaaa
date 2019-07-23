import itertools
n,k=map(int,input().split())
a=str(n)
l=list(itertools.combinations(a,len(a)-k))
l.sort()
print(*l[0],sep="")
