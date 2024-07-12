N, M = map(int, input().split())
lst = []
for n in range(N):
    tmp = list(map(int, input().split()))
    lst.append(sorted(tmp))

maxV = []
for l in lst:
   maxV.append(l[0]) 
max_value = max(maxV)
max_index = maxV.index(max_value)

print(max_value)