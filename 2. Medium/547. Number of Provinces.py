    
    
def findCircleNum(isConnected: list[list[int]]) -> int:
    num_city = len(isConnected)
    visited = [False] * num_city
    ans = 0

    def dfs(city):
        visited[city] = True

        for neb in range(num_city):
            if isConnected[city][neb] and visited[neb] != True:
                dfs(neb)


    for city in range(num_city):
        if not visited[city]:
            dfs(city)
            ans += 1
    
    return ans


print(findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))