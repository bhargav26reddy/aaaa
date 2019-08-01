n,m=map(int,input().split())
l=list(map(int,input().split()))
for i in range(m):
    v,k=map(int,input().split())
    print(sum(l[v-1:k]))
