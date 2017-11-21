# http://rosalind.info/problems/subs/

sample = input("sample = ")
substring = input("substring = ")
start = 0
stop = len(substring) # create a search space the same size as the substring
results = []

def SubstringSearch(sample,substring,start,stop,results):
    if sample[start:stop] == substring: # if the search space  contains the substring
    	results.append(str(start + 1)) # add the location of the first letter to the results
    start += 1
    stop += 1 # move the search space one letter to the right
    if stop <= len(sample): # if the entire sample hasn't been searched yet
        SubstringSearch(sample,substring,start,stop,results) # search the new search space

SubstringSearch(sample,substring,start,stop,results)

print(" ".join(results)) # print the results formatted per the instructions
