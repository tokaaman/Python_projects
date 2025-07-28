ask=input("inter the word you want")
p=ask.upper()
c=""
for i in range(len(p)):
	if p[i]=="A" or p[i]=="E" or p[i]=="I" or p[i]=="O" or p[i]=="U":
		continue 
	c+=p[i]	
print(c)	
	
