def dfs(graph,node):
    visited=set()
    def dfs_helper(graph,node):
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graph[node]:
                dfs_helper(neighbor)
    dfs_helper(graph,node)
graph={'A':['B','C'],'B':['A','D','E'],'C':['A','F'],'D':['B'],'E':['B','F'],'F':['C','E']}
dfs(graph,'A')