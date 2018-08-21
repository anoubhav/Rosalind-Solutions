from math import factorial
with open(r'D:\Downloads\rosalind_pmch (1).txt') as f:
    temp = f.readlines()
    strand = ''
    for line in temp:
        if '>' not in line:
            strand += line.strip()
    print(strand)
    m = strand.count('A')
    n = strand.count('C')
    print(factorial(m)*factorial(n))