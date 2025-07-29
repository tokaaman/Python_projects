print("Welcome to my python calculator")
def add(a,b):
	return a+b
def minus(a,b):
	return a-b
def mult(a,b):
	return a*b
def div(a,b):
	return a/b
oper={
"+":add,
"-":minus,
"*":mult,
"/":div
}
def calculator():	
	frist=float(input("enter frist number : "))
	for x in oper:
		print(x)	
	opr=input("pick a operator : ")
	second=float(input("write second : "))
	operation=oper[opr]
	sum=operation(frist, second)
	print(sum)
	while 2!=3:
		w=input(f"if you want to add another operation to {sum} type 'y' if not 'n' : ")
		if w=="y":
		       for x in oper:
		            print(x)
		       opr=input("pick a operator : ")     	
		       another=float(input("write another number : "))	
		       sum=oper[opr](sum,another)
		       print(sum)
		else:
			break
	calculator()		
calculator()		       																