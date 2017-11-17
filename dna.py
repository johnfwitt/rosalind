#http://rosalind.info/problems/dna/

sample = input("sample: ")
result = ""

result += str(sample.count('A')) + " "
result += str(sample.count('C')) + " "
result += str(sample.count('G')) + " "
result += str(sample.count('T'))

print(result)