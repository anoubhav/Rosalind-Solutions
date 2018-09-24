def codonTable():
    keys = list()
    values = list()
    with open(r'rna_codon_table.txt') as f:
        for line in f.readlines():
            arr = line.strip().split(' ')
            arr = [a for a in arr if len(a)>0]
            keys = keys + arr[0::2]
            values = values +arr[1::2]
        table = dict(zip(keys, values))
        return table
