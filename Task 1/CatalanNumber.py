# Python Program for nth Catalan Number

# Catalan numbers form a sequence of natural numbers
# that occur in various counting problems. Particularly, 
# count the number of expressions containing n pairs of
# parentheses which are correctly matched.
# For n = 3, possible expressions are 
# ((())), ()(()), ()()(), (())(), (()()).
# The first Catalan numbers for n = 0, 1, 2, 3, ... are
# 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …

# Catalan numbers satisfy the recurrence relations (see wiki)
# and can be written as
# C[0] = 1
# C[1] = 1
# C[2] = C[0]*C[1] + C[1]C[0] = 2
# C[3] = C[0]*C[2] + C[1]C[1] + C[2]C[0] = 5
# C[4] = C[0]*C[3] +  C[1]C[2] + C[2]C[1] + C[3]C[0] = 14
# C[5] = C[0]*C[4] +C[1]*C[3]+ C[2]*C[2] +  C[3]*C[1] + C[4]*C[0] = 42
# etc.


def catalan(n): 
	if (n == 0 or n == 1): 
		return 1
	# Table to store results of subproblems 
	C = [0 for i in range(n + 1)] 
	# Initialize first two values in table 
	C[0] = 1
	C[1] = 1
	# Fill entries in catalan[] using recursive formula 
	for i in range(2, n + 1): 
		C[i] = 0
		for j in range(i): 
			C[i] = C[i] + C[j] * C[i-j-1] 
	# Return last entry 
	return C[n] 
# Driver code
if __name__ == "__main__": 
	n = int(input("Input: ")) 
	print(catalan(n)) 
 
