def factorial_while(value):
		answer = 1
		while value > 1:
			answer *= value
			value -= 1
			# print("val",value," ans",answer)
		return answer

def factorial_for(value):
	for x in range(1,value):
		value *= x
	return value

def factorial_recursion(value):
	return value * factorial_recursion(value - 1)

def recur_factorial(value):
   if value == 1:
       return value
   else:
       return value * recur_factorial(value - 1)	
	
userinput = input("Enter a whole number: ")

try:
	userinput = int(userinput)	
except:
	print("Error")
else:
	if userinput == 0:
		print("not zero")
	elif userinput == 0 or userinput == 1:
		print(1)
	else:
		print("while",factorial_while(userinput))
		print("for",factorial_for(userinput))
		print("recursion",recur_factorial(userinput))

