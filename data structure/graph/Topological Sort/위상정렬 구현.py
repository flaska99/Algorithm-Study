from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

in_degree = [0] * (n+1) #진입차수

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

queue = deque()
result = []

for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    result.append(now)
    
    for next_node in graph[now]:
        in_degree[next_node] -= 1
        if in_degree[next_node] == 0:
            queue.append(next_node)