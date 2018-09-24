from codon_table import codonTable
codon_dict = codonTable()

with open(r'D:/Downloads/rosalind_prot (2).txt') as f:
    rna = f.readline().strip()
    rna_len = len(rna)
    # print(rna_len)
    arr = [codon_dict[rna[i:i+3]] for i in range(0, rna_len, 3)]
    arr.remove('Stop')
    print(''.join(arr))

