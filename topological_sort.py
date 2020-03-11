def topological_sort(graph):
    numNodes = len(graph)
    
    stack = []
    topologically_sorted = []

    #count is used to detect if a topological sort is possible or not, i.e if there is a cycle in the directed graph or not
    count = 0
    
    #calculate the indegree
    for i in range(numNodes):
        indegree = [len(graph[i]) for i in graph.keys()]
    
    #choose the nodes with no dependency and add them to the stack
    for i,degree in enumerate(indegree):
        if degree == 0:
            stack.append(i)
            
    while stack:
        current = stack.pop()
        topologically_sorted.append(current)
        count+=1 

    #check which nodes depend on the selected nodes and decrease their indegrees by 1
        for key in graph.keys():
            for val in graph[key]:
                if current == val:
                    indegree[key] -=1
                    if indegree[key] == 0:
                        stack.append(key)


    print("The topological sort is valid " if count == numNodes else "No Topological Sort possible")             
    return topologically_sorted


adj_list = {0: [1, 2], 
            1: [3], 
            2: [3], 
            3: []}

print(topological_sort(adj_list))