# http://rosalind.info/problems/hamm/
# The variables are outlined in the puzzle above.

s = raw_input("s = ? ")
t = raw_input("t = ? ")
hamDist = 0
n = 0 # the current index to be checked

while n < len(s):
    if s[n] != t[n]:
        hamDist += 1
    n += 1

print hamDist
