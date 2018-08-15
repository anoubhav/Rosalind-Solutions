import re
with open(r'D:/Downloads/rosalind_cons (2).txt') as f:
    with open('answer.txt', 'w') as wf:
        full = f.read()
        res = re.split(r'>Rosalind_[0-9]+\n', full)[1:]
        l = len(res[0].strip().replace('\n', ''))

        profile_mat = {'A':[0]*l, 'C':[0]*l, 'T':[0]*l, 'G':[0]*l}

        for strand_unedited in res:
            strand = strand_unedited.strip().replace('\n', '')
            # l == len(strand)
            for i in range(l):
                profile_mat[strand[i]][i] += 1
        
        v = list(profile_mat.values())
        compare_lst = zip(v[0], v[1], v[2], v[3])

        # Consensus string
        consensus = list()
        for i in compare_lst:

            val, idx = max((val, idx) for (idx, val) in enumerate(i))
            temp = dict(zip('0123', 'ACTG'))
            consensus.append(temp[str(idx)])

        # Writes the profile matrix and consensus string into answer.txt

        wf.write(''.join(consensus))
        wf.write('\n')

        for k, v in profile_mat.items():
            profile = k + ': ' + ' '.join([str(a) for a in v])
            
            wf.write(profile)
            wf.write('\n')
