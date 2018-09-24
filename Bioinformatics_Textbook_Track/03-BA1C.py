def ReverseComplement(strand):
    """ Finds the reverse complement of a DNA string. (str) -> (str) """
    return (
        strand.replace('A', 't')
        .replace('G', 'c')
        .replace('C', 'g')
        .replace('T', 'a')
        .upper()[::-1]
    )

if __name__ == '__main__':
    strand = input()
    print(ReverseComplement(strand))