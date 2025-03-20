

def reverseWords(s):
    words = s.split()
    return " ".join(words[::-1])


if __name__ == "__main__":
    s = "the sky is blue"
    print(reverseWords(s))

    s = "  hello world  "
    print(reverseWords(s))

    s = "a good   example"
    print(reverseWords(s))

    
