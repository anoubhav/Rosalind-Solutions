import random
#  Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

# By probability
def mendel(k, m, n):
    tot = float(k + m + n)
    return (1 - (n/tot)*((n-1)/(tot-1)) - (n/tot)*(m/(tot-1)) - (m/tot)*((m-1)/(tot-1))*0.25)

print(mendel(21, 21, 19))


# By simulation ( not working, don't know reason )

# def mendel(k, m, n, sim_no):
#     count = 0
#     arr = ['k']*k + ['m']*m + ['n']*n
#     for i in range(sim_no):
#         p1 =  random.choice(arr)
#         p2 =  random.choice(arr)

        # ------------ Option 1 -------------- #
#         if p1 == 'k' or p2 == 'k':
#             count += 1
#         if p1 == 'm' and p2 == 'm':
#             count += random.choice([1, 1, 1, 0])
#         if p1 == 'm' and p2 == 'n':
#             count += random.choice([1, 0])
        # if p1 == 'n' and p2 == 'm':
#             count += random.choice([1, 0])
    # return count/sim_no

        # ------------ Option 2 -------------- #
#         if p1 == 'n' and p2 == 'n':
#             count += 1
#         if p1 == 'm' and p2 == 'n':
#             count += random.choice([1, 0])
#         if p1 == 'n' and p2 == 'm':
#             count += random.choice([1, 0])
#         if p1 == 'm' and p2 == 'm':
#             count += random.choice([0, 0, 0, 1])
#     return 1 - count/sim_no

# print(mendel(2, 2, 2, 100000))