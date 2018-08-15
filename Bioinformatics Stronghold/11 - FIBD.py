import math
def mortal_rabbits(n, m):
    # n is the no.of months and m is the lifespan of the rabbits
    labels_lst = [i for i in range(2,100000)]
    population = {1:1}
    # print(f'--------- month 1 ---------')
    # print(population)
    count = 1
    for i in range(2,n+1):
        keys = list(population.keys())
        for k in keys:
            if population[k] == 1:
                population[k] += 1
            elif population[k] == m:
                population[k] = 1
            else:
    
                count = count + 1
                population[k] += 1
                population[count] = 1
        print(f'--------- month {i} ---------')
        print(population)
        # print(i, len(population))
    return len(population)

# print('\nNo. of alive rabbits:',mortal_rabbits(9,3),'\n')

def mortal_rabbits(n, m):
    sequence = [1, 1]

    for i in range(n - 2):
        new_num = 0
        if i + 2 < m:
            #Normal fibonacci - No deaths yet
            new_num = sequence[i] + sequence[i + 1]
        else:
            #Different reoccurence relation - Accounting for death
            for j in range(m - 1):
                new_num += sequence[i - j]

        sequence.append(new_num)

    return sequence[-1]

print('\nNo. of alive rabbits:',mortal_rabbits(86,16),'\n')
