

with open(r'D:\Downloads\rosalind_revc(1).txt') as f:
    s = f.read().strip()

    """ 
    Method 1
     """
    s_rev = s[::-1]
    lst = list()
    for i in range(len(s_rev)):
        if s_rev[i] == 'G':
            lst.append('C')
            continue
        if s_rev[i] == 'C':
            lst.append('G')
            continue
        if s_rev[i] == 'A':
            lst.append('T')
            continue
        if s_rev[i] == 'T':
            lst.append('A')
            continue
    # print(''.join(lst))

    """ 
    Method 2
     """
    
    lst = list()
    # complement = dict(zip('ACGT', 'TGCA'))
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    for i in s[::-1]:
        lst.append(complement[i])
    # print(''.join(lst))


    """ 
    Method 3 
    """

    # $ cat rosalind2.txt | tr 'ACGT' 'TGCA' | rev
    # rev commmand not able to recognize on cmd


    """ 
    Method 4
     """
    
    # print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))

    """ 
    Method 5
     """

    result = s.replace('A','t').replace('G','c').replace('C','g').replace('T','a').upper()[::-1]
    print(result)