
# Time complexity = O(C(n,k).k) # since there ate C(n,k) combinations, additional k is time spent modifying comb list
# SPace complexity : O(C(n,k).k) # store C(n,k) combinations each of size k, because k elements stored at a time
def combination(n, k):
    output = []

    def backtracking(start, comb):

        if len(comb) == k:
            output.append(comb[:])
            return

        for i in range(start, n+1):
            comb.append(i)
            backtracking(i+1, comb) 
            # first recursive backtracker i, i.e i1 = 1, add it in comb then we go to 2nd recursive backtracker, i2=2,  
            # add it in comb, at third recursive backtracker, i3=3, len(conb)==k so comb, (1,2) is append in output, then go out of 3rd backtracker to 2nd, and pop i2=2, i2=3 now,
            #  and append 3 in comb to make (1,3) and append in output, then pop 3 and push 4, to make (1,4)....and continue
            comb.pop()
        
    backtracking(1, [])
    return output










if __name__=="__main__":
    n = 4
    k = 2

    print(combination(n, k))

