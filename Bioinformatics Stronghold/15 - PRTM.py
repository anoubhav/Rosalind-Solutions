with open('monoisotopic mass table.txt') as f:
    lines = f.readlines()
    aa_weight = dict()

    for line in lines:
        a, b = line.split()
        aa_weight[a] = float(b)
    
    s = input('String:\n')
    tot = 0
    for i in s:
        tot += aa_weight[i] 
    print(tot)
