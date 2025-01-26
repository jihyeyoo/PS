from collections import deque,defaultdict
def solution(n, edge):
    graph = defaultdict(list)
    for i in range(len(edge)) :
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])
    
    Q = deque()
    Q.append(1)
    Visited = [10e9 for _ in range(n+1)]
    Visited[1] = 0
    
    while Q :
        cur_node = Q.popleft()
        for next_node in graph[cur_node] :
            if Visited[next_node] <= Visited[cur_node] + 1 :
                continue
            Visited[next_node] = Visited[cur_node] + 1
            Q.append(next_node)
    
    Visited.sort(reverse=True)
    max_val = 0
    
    for i in range(len(Visited)) :
        if Visited[i] == 10e9:
            Visited.remove(Visited[i])
        else:
            break
        
    return Visited.count(max(Visited))
