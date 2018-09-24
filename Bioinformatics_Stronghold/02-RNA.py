with open(r'D:/Downloads/rosalind_rna.txt') as f:
    s = f.read()
    rna_s = s.replace('T', 'U')
    print(rna_s)

# No need to leave the shell
# cat rosalind_rna.txt | tr T U