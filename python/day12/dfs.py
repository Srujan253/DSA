visited=set()
def dfs_helper(graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs_helper(graph, neighbor)
    
graph={'A':['B','C'],'B':['A','D'],'C':['A','D'],'D':['B','C','E'],'E':['B','D']}
dfs_helper(graph,'A')