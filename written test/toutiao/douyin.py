import sys
 
 
def dfs(g, x, y, visited):
    n = len(g)
    visited[y] = True
    for i in range(n):
        if i != y and g[y][i] == 1 and g[x][i] == 0 and not visited[i]:
            g[x][i] = 1
            dfs(g, x, i, visited)
    return
 
 
if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
 
    temp_relation = list(map(int, sys.stdin.readline().strip().split()))
    relation = [[0 if i != j else 1 for i in range(n)] for j in range(n)]
    for i in range(m):
        relation[temp_relation[2 * i] - 1][temp_relation[2 * i + 1] - 1] = 1
 
    for i in range(n):
        visited = [False for i in range(n)]
        for j in range(n):
            if i != j and relation[i][j] == 1 and not visited[j]:
                dfs(relation, i, j, visited)
 
    relation = list(zip(*relation))
    count = 0
    for i in range(n):
        flag = True
        for j in range(n):
            if relation[i][j] == 0:
                flag = False
                break
        if flag:
            count += 1
    print(count)