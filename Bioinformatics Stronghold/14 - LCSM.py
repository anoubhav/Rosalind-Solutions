with open(r'D:/Downloads/rosalind_.txt') as f:
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