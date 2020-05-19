
table = list(map(int, "0110100110010110100101100110100110010110011010010110100110010110100101100110100101101001100101100110100110010110100101100110100110010110011010010110100110010110011010011001011010010110011010010110100110010110100101100110100110010110011010010110100110010110"))


# Function to find the parity 
def Parity(num) : 

	# Number is considered to be 
	# of 32 bits 
	max = 16

	# Dividing the number o 8-bit 
	# chunks while performing X-OR 
	while (max >= 8): 
		num = num ^ (num >> max) 
		max = max // 2
    
	print(table)
	# Masking the number with 0xff (11111111) 
	# to produce valid 8-bit result 
	return table[num & 0xff] 

# Driver code 
if __name__ =="__main__": 
	num = 11
	
	# Result is 1 for odd parity, 
	# 0 for even parity 
	result = Parity(num)
	print(result)
	print("Odd Parity") if result else print("Even Parity") 
