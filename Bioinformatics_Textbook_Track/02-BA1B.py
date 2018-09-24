from collections import defaultdict

def MostFreqKmer(dna, k):
    """ Finds the most frequent k-mers in a string 
    (str, int) -> (list of str) """
    l = len(dna)
    kmer_count = defaultdict(int)

    for i in range(l - k + 1):
        kmer_count[dna[i:i+k]] += 1

    temp = max(kmer_count.values())

    return ' '.join([k for k, v in kmer_count.items() if v == temp])

if __name__ == '__main__':
    dna = input()
    k   = int(input())
    print(MostFreqKmer(dna, k))
