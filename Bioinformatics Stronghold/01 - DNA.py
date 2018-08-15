with open(r'D:\Downloads\rosalind_dna.txt') as f:
    base_string = f.read()
    print(base_string.count('A'))
    print(base_string.count('C'))
    print(base_string.count('G'))
    print(base_string.count('T'))

    # map object returns an iterator. The * allows normal functions like print to access the iterator elements

    # print(*map(base_string.count, "ACGT"))