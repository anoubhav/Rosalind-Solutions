def read_fasta(fname):
    """ Reads the FASTA file and returns the Rosalind_ID and sequence as a tuple of lists
    (str) -> (list, list) """
    dna = dict()
    with open(fname) as f:
        while True:
            try:
                line = f.readline()
                if line[0] == ">":
                    label = line[1:].strip()
                    dna[label] = ""
                else:
                    dna[label] += line.strip()
            except (EOFError, IndexError):
                break

    return list(dna.keys()), list(dna.values())