# http://rosalind.info/problems/iprb/

k = float(input("k = ? ")) # homozygous dominant XX
m = float(input("m = ? ")) # heterozygous Xx
n = float(input("n = ? ")) # homozygous recessive xx
oda = 0.0 # oda = offspring with dominant alleles

pop = k + m + n # pop = the total population
perms = pop * (pop - 1) # the number of ways we can arrange the individuals; permutations

oda += (k * (pop-1)) # k can combine with pop-1 individuals, all combos produce oda
oda += m*k # when m combines with k, it produces oda
oda += 0.75*m*(m-1) # m and m have a 3/4 chance of producing oda
oda += m*n*0.5 # m and n have a 1/2 chance of producing oda
oda += n*k # n and k always produce oda
oda += n*m*0.5 # n and m have a 1/2 chance of producing oda
# n and n never produce oda.

odds = oda / perms
print odds

# Lines 11-17 could have been written on one line, but there were a lot of factors to juggle,
# and I feel writing it this way makes it both easier to read and to check for mistakes.
