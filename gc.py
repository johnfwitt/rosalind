# http://rosalind.info/problems/gc/
# the input file will need to be renamed "samples.txt" and moved to the same folder as this script

import os

contentList = [] # this will be used as a list of GC percentages

with open ("samples.txt", "r") as myfile:
    samples = myfile.read().replace('\n','') # read the content of the file as a string

# each sample is separated by the character '>'
samples = samples.split('>') # split the samples up into a list 
samples.pop(0) # this results in an empty first item; drop it

for sample in samples:
    # determine the GC percentage of each sample
    gcCount = sample.count('C') + sample.count('G')
    gcContent = (gcCount / (len(sample) - 13)) * 100 # the sample labels are 13 characters long; we don't want to include them
    contentList.append(gcContent) # add this to our list of percentages

# find the sample with the highest GC content and format the result
result = samples[contentList.index(max(contentList))][:13] + "\n" + str(max(contentList))

print(result)
