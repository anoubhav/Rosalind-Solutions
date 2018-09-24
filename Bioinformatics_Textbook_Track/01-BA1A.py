def PatternCount(text, pattern):
    """ We define PatternCount(Text, Pattern) as the number of times that a k-mer Pattern appears as a substring of Text.  
    (str, str) -> (int) """
    l_p = len(pattern)
    l_t = len(text)
    tot = 0
    for i in range(l_t - l_p + 1):
        if text[i:i+l_p] == pattern: tot += 1
    return tot

if __name__ == '__main__':
    text    = input()
    pattern = input()
    print(PatternCount(text, pattern))

