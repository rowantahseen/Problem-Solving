def bfs(graph,root):
    # root (0,0) node 0
    Q = [root]
    V = set()
    l = len(graph[0])
    while Q:
        current = Q.pop(0)
        if current not in V:
            V.add(current)

            # ------ in case of adj_matrix (Comment the below section) ------
            for i,neighbour in enumerate(graph[current]):
                if neighbour == 1 and i not in V:
                    Q.append(i)
            print("Node : " , current)

            # ----- in case of adj_list (Comment the above section) ------
            for i,neighbour in enumerate(graph[current]):
                if neighbour not in V:
                    Q.append(neighbour)
            print("Node : " , current)

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
bfs(adj_list,root)
# Output should be  0, 1 ,4 ,2 , 3 

