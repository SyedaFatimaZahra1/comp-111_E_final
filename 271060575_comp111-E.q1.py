def dec_to_bin(num):
	if num >= 1:
		dec_to_bin(num // 2)
	print(num % 2)
num_input = 20
print(f"{num_input} converted to binary is: " )
print(dec_to_bin(num_input))		

		