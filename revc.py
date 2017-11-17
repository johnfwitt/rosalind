# http://rosalind.info/problems/revc/

sample = input("sample = ")

step1 = sample[::-1]
step2 = step1.replace('A','1').replace('C','2').replace('G','3').replace('T','4')
result = step2.replace('1','T').replace('2','G').replace('3','C').replace('4','A')

print (result)

# str.replace('A','T').replace('C','G').replace('G','C').replace('T','A') won't work.
# It does these steps one at a time, so at the end you end up with all C's and T's.
# The numbers act as 'middle men' to avoid this problem.