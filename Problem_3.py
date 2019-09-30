#unique factorization
#based on fundamental theorem of arithmetic
big_number = 600851475143 

a = []               
f = 2                
while big_number > 1:        
	if big_number % f == 0:     
		a.append(f)         
		big_number /= f              
	else:                
		f += 1             

print(a)