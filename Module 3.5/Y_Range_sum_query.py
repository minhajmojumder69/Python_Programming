n,m = map(int,input().split())
array = list(map(int,input().split()))
prefix = [0]* (n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + array[i]

for j in range(m):
    a,b = map(int,input().split())
    print(prefix[b] - prefix[a-1])
