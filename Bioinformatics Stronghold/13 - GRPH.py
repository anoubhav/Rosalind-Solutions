with open(r'D:/Downloads/rosalind_grph (3).txt') as f:
    with open(r'answers.txt', 'w') as wf:
        a = f.readlines()

        # Obtaining labels and strands in list
        labels = list()
        strands = list()
        strand = ''

        for line in a:
            if 'Rosa' in line:
                labels.append(line[1:].strip())
                strands.append(strand)
                strand = ''
            else:
                strand += line.strip()

        strands.append(strand)
        del strands[0]

        # Obtaining prefix and suffix and label in a list of tuples
        lab_pre_suf = [(labels[i],strands[i][:3], strands[i][-3:]) for i in range(len(strands))]
        print(lab_pre_suf)

        # Comparing to check which strands prefix == other strands suffix
        result = list()
        for i in lab_pre_suf:
            for j in lab_pre_suf:
                if j!=i:
                    if i[2] == j[1]:
                        wf.write(f'{i[0]} {j[0]}\n')
                    # result.append(f'{i[0]} {j[0]}')
    

