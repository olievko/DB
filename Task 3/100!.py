# Python program to find sum of digits in factorial of a number 
 
# Function to multiply x with large number 
# stored in vector v. Result is stored in v. 
def multiply(v, x): 
	carry = 0
	size = len(v) 
	for i in range(size): 	
		# Calculate res + prev carry 
		res = carry + v[i] * x 
		# updation at ith position 
		v[i] = res % 10
		carry = res // 10
	while (carry != 0): 
		v.append(carry % 10) 
		carry //= 10

# Returns sum of digits in n! 
def SumDig( n): 
	v = []	 # create a vector of type int 
	v.append(1) # adds 1 to the end 

	# One by one multiply i to current 
	# vector and update the vector. 
	for i in range(1, n + 1): 
		multiply(v, i) 

	# Find sum of digits in vector v[] 
	sum = 0
	size = len(v) 
	for i in range(size): 
		sum += v[i] 
	return sum

# Driver code 
if __name__ == "__main__": 
	
	n = int(input("Input: "))
	print("Output:", SumDig(n)) 
