# http://rosalind.info/problems/fib/
# the variables and their meanings are outlined in the puzzle

n = input("n = ? ")
k = input("k = ? ")
f = [1,1]

while len(f) < n:
    f += [f[len(f)-1] + k * f[len(f)-2]]

print f[n-1]

# a for loop may have been better here
# I may revise this in the future
