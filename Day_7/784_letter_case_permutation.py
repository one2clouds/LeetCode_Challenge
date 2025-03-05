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



if __name__=="__main__":
    string_S = 'a1b1'
    print(letter_case_permutation(string_S))

