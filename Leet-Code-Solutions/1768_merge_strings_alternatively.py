#Time Complexity : O(n+m) # n= letter of word1 & m = letter of word2
# Space Complexity : O(n+m) # 


def merge_string_alternatively(word1, word2):

    min_length = min(len(word1), len(word2))
    output = []

    for i in range(min_length):
        output.append(word1[i])
        output.append(word2[i])

    # append after all words after min_length
    output.append(word1[min_length:])
    output.append(word2[min_length:])

    # return list of character as string
    return "".join(output)


if __name__=="__main__":
    word1 = "abcd"
    word2 = "pqrstuv"
    print(merge_string_alternatively(word1, word2))
