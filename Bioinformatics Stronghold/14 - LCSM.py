from fasta_reader import read_fasta
 
def LCS( text ):
    for k in range(len(text[0]),1,-1):
        for start in range(len(text[0])-k+1):
            curr = text[0][start:start+k]
            found = True
            for i in range(1,len(text)):
                if not curr in text[i]:
                    found = False
                    break
            if found:
                return curr

if __name__ == '__main__':
    _, sequences = read_fasta(r'D:/Downloads/rosalind_lcsm.txt')
    print(LCS(sequences))