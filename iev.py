# http://rosalind.info/problems/iev/
# ODA = offspring with dominant alleles

sample = input("sample = ")
result = 0

samples = sample.split() # split the sample up into a list

# Find the number of ODA-producing parents of each type by multiplying the number of pairs by their chance of producing ODA
# Multiply that number by the number of offspring they will produce (2)
# Add that number to the total expected ODA of the population

result += (float(samples[0]) * 1) * 2 # The first three pairs have at least one homozygous dominant parent and will always produce ODA; AA-AA
result += (float(samples[1]) * 1) * 2 # AA-Aa
result += (float(samples[2]) * 1) * 2 # AA-aa
result += (float(samples[3]) * .75) * 2 # Two heterozygous parents have a 75% chance of producing ODA; Aa-Aa
result += (float(samples[4]) * .5) * 2 # One heterozygous and one homozygous recessive parent have a 50% chance of producing ODA; Aa-aa
# two homozygous recessive parents do not produce ODA and are not added to the result; aa-aa

print (result)

# this is another solution that I think is more readable and easier to check for errors when separated into several lines of code
