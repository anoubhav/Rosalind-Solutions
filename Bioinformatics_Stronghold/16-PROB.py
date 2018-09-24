from math import log10
s = input('String:\n')
# Below statement not working--> ValueError: could not convert string to float: '.'
# gc_content = input('GC:\n')
gc_content = '0.075 0.147 0.177 0.233 0.275 0.310 0.380 0.444 0.498 0.534 0.578 0.635 0.679 0.703 0.786 0.804 0.885 0.939'
gc_content = [float(i) for i in gc_content.split()]

base_proba = dict()
result = list()
for i in gc_content:
    base_proba['G'], base_proba['C'] = i/2, i/2
    base_proba['A'], base_proba['T'] = (1-i)/2, (1-i)/2

    tot_logprob = 0
    for i in s:
        tot_logprob += log10(base_proba[i])
    result.append(tot_logprob)
print(' '.join([str(round(i,3)) for i in result]))
    

    
