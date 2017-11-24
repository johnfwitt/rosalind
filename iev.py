# http://rosalind.info/problems/iev/
# ODA = offspring with dominant alleles

sample = input("sample = ")
result = 0

samples = sample.split() # separate the samples into a list

# find the number of each parent pair type that will produce ODA by multiplying the total number of pairs by their chance of producing ODA
# multiply that number by the number of expected offspring (2)
# add it to the total number of ODA produced by all pair types

result += (float(samples[0]) * 1) * 2 # The first three pairs have at least one homozygous dominant parent and will always produce ODA
result += (float(samples[1]) * 1) * 2
result += (float(samples[2]) * 1) * 2
result += (float(samples[3]) * .75) * 2 # Two heterozygous parents have a 75% chance of producing ODA
result += (float(samples[4]) * .5) * 2 # One heterozygous and one homozygous recessive parent have a 50% chance of producing ODA
# two homozygous recessive parents do not produce ODA and are not added to the result

print (result)

# this is another solution that I think is more readable and easier to check for errors when separated into several lines of code
