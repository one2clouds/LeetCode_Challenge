# a hard question of "union find" algorithm, see question 547 for medium solution
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
                            
    def find_parent(self, x):
        res = x
        while res != self.parent[res]:
            res = self.parent[res]
        return res
    
    def union(self, x, y):
        par_x, par_y = self.find_parent(x), self.find_parent(y)

        if par_x == par_y:
            return 0
        
        if self.size[par_x] > self.size[par_y]:
            self.size[par_x] += self.size[par_y]
            self.parent[par_y] = par_x
        else:
            self.size[par_y] += self.size[par_x]
            self.parent[par_x] = par_y

        return 1



# 1) combine the connected node in the 1st step 
# 2) Get cost for each component, we need to return minimum const for walking from node i to j, and from question, it says the cost of 
# walking from each node will be bitwise-and operation, so we do bitwise-and while calculating cost if that node is already seen in component_cost_hashmap
# 3) we will just check for the node r1 and r2 in the component_cost_hashmap if parents node for r1 and r2 are different or same, if same return cost value, 
# and if different return -1 as they are not connected


# 1) for travelling from 
def minimum_Cost(n, edges, query):

    # 1) Building unions
    uf = UnionFind(n)
    for u, v, w in edges:
        uf.union(u, v)

    # 2) Get cost for each component
    component_cost_hash = {}
    for u, v, w in edges:
        root = uf.find_parent(u)

        if root not in component_cost_hash:
            component_cost_hash[root] = w
        
        else:
            component_cost_hash[root] &= w

    # 3) Queries
    result = []

    for src, dst in query:
        r1, r2 = uf.find_parent(src), uf.find_parent(dst)

        if r1 != r2:
            result.append(-1)
        else:
            result.append(component_cost_hash[r1])

    return result



if __name__ == "__main__":
    n = 5
    edges = [[0,1,7],[1,3,7],[1,2,1]]
    query = [[0,3],[3,4]]

    print(minimum_Cost(n, edges, query))

    n = 3
    edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
    query = [[1,2]]

    print(minimum_Cost(n, edges, query))



    

    


