"""
Backtracking : 
problem solving algorithm technique , involves finding 
solution incrementally by trying different options and 
undoing them if they lead to dead end
"""

# Iterative approach 
# Time O(2^n) & Space O(2^n)
def letter_case_permutation(string_S): 
    outputs = [""] # empty string executes once in a loop

    for s in string_S:
        tmp = []
        for o in outputs:
            if s.isalpha():
                tmp.append(o + s.lower())
                tmp.append(o + s.upper())
            else:
                tmp.append(o+s)
        outputs = tmp # tmp after first iteration contains [a, A], so we need to start after that and not empty string

    return outputs

# Recursive Approach 
# Time O(2^n) & Space O(N+ 2^n)
def letter_case_permutation_recursive(string_S):
    res = []
    def back_tracking(sub_str="", i=0):
        if len(sub_str) == len(string_S):
            res.append(sub_str)
            return # get out if substring == string_S and append to main list
        
        if string_S[i].isalpha():
            back_tracking(sub_str+string_S[i].swapcase(), i+1) # recursive until the len(sub_str) == len(string_S) for each of upper and lower string and each numbers. 

        back_tracking(sub_str+string_S[i], i+1)

    back_tracking()
    return res



if __name__=="__main__":
    string_S = 'a1b1'
    print(letter_case_permutation(string_S))
    print(letter_case_permutation_recursive(string_S))

