file_name = 'rosalind_gc (3).txt'
max_label, max_gc, gc_tot, tot_len = 0, 0, 0, 0

with open(f'D://Downloads//{file_name}') as f:
    for line in f.readlines():
        if '>' in line:

            try:
                gc_percentage = 100*gc_tot/tot_len
                if(gc_percentage > max_gc):
                    max_gc = gc_percentage
                    max_label = label
                gc_tot, tot_len = 0, 0
            except:
                pass

            label = line.replace('>', '').strip()
        else:
            gc_tot = gc_tot + line.count('G') + line.count('C')
            tot_len = tot_len + len(line.strip())

    print(max_label, max_gc)


#     a = f.readlines()
#     for i in a[:17]:
#         # print(i)
#         if '>' in i:
#             continue
#         gc_tot = gc_tot + i.count('G') + i.count('C')
#         tot_len = tot_len + len(i.strip())
#     print(tot_len)
#     print(gc_tot)



# line = 'CGCCCGGCTCAGGGTTCGCTTGTGGCGCGCAGGAGTGACTCAACCAGGCAGTGATCGGACCAAGTAGTCACAAGTCTGAAAAAAGTAGAGTGACTCCGTGTCGCCGGTTAATCTGCGCTGTACCAATACCCGCATGCAGGAACGGAAGTCCAGTGTGGTTAAGCTTACGTGAGCTTACGCGAATCTATATCCGATCGGTTCAGACCAAGGTGTAATTATTTAATGAGCGGGCAAGTGGGCCACGTGTTGTGACGTAGCGTTTCCCATAGTGGCTCTCATGAGCTGCATCAGCTGTTTTCCCTCTGTGGATAGATAGCCTCGAAACTGGCACTCACTCGGCCACCACCGCCGTAGAGCTAGAGTTGGGAACGACGCCATAGGGATCGAGTCCTGGCAATCACCGAGTTCGCGAACCGGTCACAAGATAGGACCGATACCGTGTCGACATGACCGATACTACGACTAAACGGAGCTTTATTAGTCTTAACAGAGGCTTGACACGGTAAGGCCCGCACGCAGCGGGGCTGCATCGATCGTTTATACGGGCTTTTGGGCAGGCTGGATCTGCGAAACGAGTATCACAGGCATTCAGAGATCTGGGTGTTTTGCTTTCATGCTCACATTCATCGCTCCTTAATCGACTACGACCGGGAGATGGCTCGCCCCTGACGAGACCTTTTTAATAGCCGAAATGTACGACGGTGAGCTGATATCATGGAGTCAGTACAGCCTCAATGGTTGCAACGATAGACATTTTGTATAGAGCTACTTATGGGACTCTATTCATTGGAGGTAGCTCCCGATGGGGAAATAGCTAGTGATAACATTAATCCGTTCATTATGTGGGCGATTCGGCCTCAGTAAATGCTTTTTATCAGTCTCCAAGCGCGTTCCGACTCTACTATGGACATATGGGATATAATAAAATACAAC'
# print(len(line))

# print(line.count('G') + line.count('C'))