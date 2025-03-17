import collections

def num_islands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        n_rows, n_cols = len(grid), len(grid[0])
        num_islands = 0
        visit = set()

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft() 
                directions = [0,-1], [0,1], [1,0], [-1,0]   # left, right, up, down

                for d_r, d_c in directions:
                    r,c = row + d_r, col + d_c # check if there are other lands[1] on left, right, up, down of index
                    if (r in range(n_rows) and 
                    c in range(n_cols) and
                    (r,c) not in visit and 
                    (grid[r][c]=="1")):     # append in queue list and visited set only if it is a valid row, column, not in visit set and is land[1]
                        q.append((r,c))
                        visit.add((r,c))


        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)  # run bfs code to check if node in left, right, up, down of current island[1]
                    num_islands +=1
        return num_islands





if __name__ == "__main__":
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(num_islands(grid))



