# use union find method to solve the problem. 

def find_provinces(is_connected):

    n = len(is_connected[0])
    parent = [i for i in range(n)]
    rank = [1] * n 


    # finding the root_node of node n1. doing while loop until the node is the root node, 
    # as parent of root node is itself, and then returninig the root node, which is parent of itself
    def find(n1):
        res = n1

        while res != parent[res]:
            res = parent[res]
        return res
    
    # combining two node whose parents are different. Main root_node is chosen based on whether 
    # rank of node n1 vs rank of node n2. If n1's rank is higher, it will be root node for n2 and vice versa
    # return 1 if two nodes are unioned and 0 if their parents are same and didn't need union 
    def union(n1, n2):
        par1, par2 = find(n1), find(n2)

        if par1 == par2:
            return 0

        if rank[par1] > rank[par2]:
            rank[par1] += rank[par2]
            parent[par2] = par1

        else:
            rank[par2] += rank[par1]
            parent[par1] = par2
        return 1
    

    # start with n total provinces, and remember when nodes were unioned we returned 1, 
    # for every node union, decrease the final_result i.e provinces because connected 
    # components would be in a single province. And only not connected compontents would require different province. 
    final_result = n
    
    for i in range(n):
        for j in range(n):
            if is_connected[i][j]:
                final_result-= union(i, j)

    return final_result #sum(1 for i in range(n) if find(i) == i)




if __name__== "__main__":
    is_connected = [[1,1,0],[1,1,0],[0,0,1]]
    print(find_provinces(is_connected))
    is_connected = [[1,0,0],[0,1,0],[0,0,1]]
    print(find_provinces(is_connected))

