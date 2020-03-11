def dfs_iterative(graph, root):
    stack = [root]
    V = set()

    while stack:
        current = stack.pop()
        if current not in V:
            V.add(current)

            # ------ in case of adj_matrix (Comment the below section) ------ 
            for i,neighbour in enumerate(graph[current]):
                if neighbour == 1 and i not in V:
                    stack.append(i)
            print(current)

            # ------ in case of adj_list (Comment the above section) ------
            for i,neighbour in enumerate(graph[current]):
                if neighbour not in V:
                    stack.append(neighbour)
            print(current)

def dfs_recursive(graph, visited, root):
    if root not in visited:
        visited.append(root)
        print(root)
 
        # ------ in case of adj_matrix (Comment the below section) ------
        for i,neighbour in enumerate(graph[root]):
            if neighbour == 1:
                dfs_recursive(graph, visited, i)

        # ------ in case of adj_list (Comment the above section) ------
        for neighbour in graph[root]:
            print("Hi ",neighbour)
            dfs_recursive(graph, visited, neighbour)
        
        
adj_mat =[[0,1,0,0,1],
          [1,0,1,1,1],
          [0,1,0,1,0],
          [0,1,1,0,1],
          [1,1,0,1,0]]

adj_list = {0: [1, 4], 
            1: [2, 3, 4],
            2: [1, 3], 
            3: [1, 2, 4],
            4: [0, 1, 3]}
root = 0
print("OUTPUT IN ITERATEVE")
dfs_iterative(adj_list,root)

print("OUTPUT IN RECURSIVE")
visited = []
dfs_recursive(adj_mat, visited, root)