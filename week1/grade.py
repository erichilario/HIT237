'''test
this is another comment
'''
try:
	userinput = float(input("Grade: "))
except:
	print("Enter numeric values only.")
else:
	if userinput >= 0 and userinput <= 49:
		print("Fail")
	elif userinput > 50 and userinput <= 64:
		print("Pass")
	elif userinput > 64 and userinput <= 74:
		print("Credit")
	elif userinput > 74 and userinput <= 84:
		print("Distinction")
	elif userinput > 84 and userinput <= 100:
		print("High Distinction")
	else:
		print("Error")