# http://rosalind.info/problems/subs/

sample = input("sample = ")
substring = input("substring = ")
start = 0
stop = len(substring)
results = []

def SubstringSearch(sample,substring,start,stop,results):
    if sample[start:stop] == substring:
    	results.append(str(start + 1))
    start += 1
    stop += 1
    if stop <= len(sample):
        SubstringSearch(sample,substring,start,stop,results)

SubstringSearch(sample,substring,start,stop,results)

print(" ".join(results))
