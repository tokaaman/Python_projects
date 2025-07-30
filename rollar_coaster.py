height=int(input("how tall are you"))
if height>120:
	print("you can ride")
	age=int(input("what old are you"))
	if age<12:
		roll=5
	elif age>18:
		roll=12
	elif age>45 or age<50:
		roll =0	
	else:
		roll=7
	pic=input("do you want a photo write Y if yes and N foor no")
	if pic=="Y" or pic=="y":
		if age>45 and age<50:
			print("the total bill is 0")
		else:
			roll+=3
			print(f"you total bill is £{roll}")
			
			
		   
	
	else:
		print(f"you total bill is £{roll}")			
else:
	 print("you can't ride' ride")	
	 