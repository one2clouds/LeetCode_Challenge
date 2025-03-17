from collections import defaultdict

def findMissing_and_repeated_values(grid):

    hashmap = defaultdict(int) # a hashmap of integer values
    N = len(grid)

    # iterate over a grid and save grid number and their counts
    for i in range(N):
        for j in range(len(grid[0])):
            hashmap[grid[i][j]] += 1


    # iterate over the entire list to see count of double occured value, and never occured value    
    multiple_value = missing_value = 0
    for i in range(N*N + 1):
        if hashmap[i] == 2:
            multiple_value = i
        if hashmap[i] == 0:
            missing_value = i


    return [multiple_value, missing_value]



if __name__=="__main__":
    grid = [[1,3],[2,2]]
    print(findMissing_and_repeated_values(grid))
