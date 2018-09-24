def FindAllOccurences(text, pattern):
    """ Find all occurrences of a pattern in a string. (Use 0-based indexing)
    (str) -> (list of int) """
    l_p = len(pattern)
    l_t = len(text)
    indices = list()
    for i in range(l_t - l_p + 1):
        if text[i:i+l_p] == pattern: indices.append(str(i))
    return ' '.join([str(i) for i in indices])


if __name__ == '__main__':
    pattern = input()
    strand  = input()
    print(FindAllOccurences(strand, pattern))