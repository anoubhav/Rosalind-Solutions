with open(r'D:/Downloads/rosalind_subs.txt') as f:
    strings = f.readlines()
    parent_str, sub_str = strings[0].strip(), strings[1].strip()

    l = len(sub_str)
    L = len(parent_str)
    ind, a = 0, 0
    ind_lst = list()

    while 1:
        a = parent_str.find(sub_str, ind, L-1)
        if a == -1:
            break
        ind_lst.append(a + 1)
        ind = a + 1
    print(' '.join([str(i) for i in ind_lst]))

