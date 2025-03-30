## 사이클이 없어야함 (중요)
# 유니온 파인드로 구현

## 크루스칼 MST

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())
edges = []
for _ in range(m):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))

edges.sort() #크루스칼의 핵심: 코스트 오름차순 소팅..
parent = [i for i in range(n+1)]

total = 0

for cost, a ,b in edges:
    if find(parent,a) != find(parent, b):
        union(parent, a, b)
        total += cost

print(total)