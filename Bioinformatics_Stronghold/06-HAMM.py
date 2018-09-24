with open(r'D:/Downloads/rosalind_hamm (1).txt') as f:
    # Method 1
    count = 0
    s = f.readlines()
    for i in range(len(s[0])):
        if s[0][i] != s[1][i]:
            count += 1
    print(count)

    # Method 2
    print(sum(a!=b for a,b in zip(s[0], s[1])))

    # This method has 0 space complexity. Read explanation below

    # zip creates a list of tuples, so if you have two sequences of 3 billion bases, it creates an list contain 3 billion tuples, which would require gigabytes of memory (in addition to the original two sequences). izip creates an iterator which means the list is not built, and instead a function is returned, which gives you the tuples one-by-one, so you only ever have a single tuple in memory.

    # Similarly, sum([a != b for a, b in zip(s1, s2)]) builds yet another list with a list comprehension and then sums the elements. While sum(a != b for a, b in zip(s1, s2)) (note the lack of square brackets) builds a generator and so sums the elements as it goes along.
