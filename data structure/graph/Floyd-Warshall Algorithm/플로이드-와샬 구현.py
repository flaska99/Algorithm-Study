n,m = map(int, input().split())
INF = int(1e8)

dist = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    u,v,w = map(int, input().split())
    dist[u][v] = min(dist[u][v], w)
    
for k in range(1, n+1): #경유지
    for i in range(1, n+1): #출발지
        for j in range(1, n+1): #도착지
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1): 
    for j in range(1, n+1):
        if dist[i][j] == INF:
            print("INF", end=" ")
        else:
            print(dist[i][j], end=" ")
    print()