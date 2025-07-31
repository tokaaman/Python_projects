students={
"tokuma":[1,"Tokuma Aman",[90, 91, 94, 95, 96, 96], "tokkummaa@2023"],
"jibiril":[2,"Jibiril jemal", [87,87,98,90,86,91],"1234"],
 

}
def average(a):
	b=0
	i=0
	while b<6:
		b+=1
		i+=a[b-1]
	return round(i/6,2)			
def total(a):
	p=0
	q=0
	while p<6:
		p+=1
		q+=a[p-1]
	return q
def grade()	
def login():
		id=int(input("write your ID"))
		frist_name=input("write your fristname")
		password=input("write your password")
		if students[frist_name][3]==password:
			full=students[frist_name][1]
			id=students[frist_name][0]
			tota=total(students[frist_name][2])
			ava=average(students[frist_name][2])
			english=students[frist_name][2][1]
			maths=students[frist_name][2][1]
			aptitude=students[frist_name][2][1]
			biology=students[frist_name][2][1]
			chemistry=students[frist_name][2][1]
			pyesics=students[frist_name][2][1]
			print("\n\n\n\n")
			print("full name:", full)
			print("Id:", id)
			print("english",english)
			print('maths', maths)
			print("aptitude", aptitude)
			print("chemistry",  chemistry)
			print("pysics",pyesics)
			print("biology",biology)
			print("total ", tota)
			print("average",ava)	
		else:
			login()	 
login()

