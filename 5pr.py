import random
print("welcome to password generator")
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', "Y", "Z"]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
nl=int(input("enter number of the letter you want"))
ns=int(input("enter number of symbolsymbol"))
nn=int(input("enter number of whole number"))
rl=random.randint(0,51)
rn=random.randint(0,9)
rl=random.randint(0,9)
p=""
num=""
s=""
for n in range(0,nl):
	p+=alphabet[random.randint(0,51)]
for n in range(0,nn):
	num+=numbers[random.randint(0,9)]
for n in range(0,nl):
	s+=symbols[random.randint(0,9)]
all=(nl+ns+nn)-1
plas=p+num+s
password=""
for n in range(0,all):
	password+=plas[random.randint(0,all)]
print("Your new password is^",password)						