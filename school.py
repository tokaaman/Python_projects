students = {
    "tokuma": [1, "Tokuma Aman", [90, 91, 94, 95, 96, 96], "tokkummaa@2023"],
    "jibiril": [2, "Jibiril Jemal", [87, 87, 98, 90, 86, 91], "1234"],
    "leila": [3, "Leila Yusuf", [88, 85, 90, 92, 89, 91], "leila88"],
    "abdi": [4, "Abdi Kedir", [82, 84, 86, 83, 85, 87], "abdi_pass"],
    "hana": [5, "Hana Nur", [90, 91, 93, 89, 92, 94], "hana123"],
    "musa": [6, "Musa Ibrahim", [75, 78, 80, 82, 79, 77], "musa_pw"],
    "selam": [7, "Selam Tadesse", [92, 90, 95, 93, 94, 96], "selam!96"],
    "fikir": [8, "Fikir Alemu", [85, 88, 84, 87, 86, 89], "fikir_code"],
    "biruk": [9, "Biruk Desta", [70, 72, 75, 73, 71, 74], "biruk_74"],
    "lily": [10, "Lily Tesfaye", [93, 94, 95, 96, 92, 91], "lily_pw"],
    "sami": [11, "Sami Mohammed", [68, 70, 69, 71, 67, 72], "sami_login"],
    "betty": [12, "Betty Awoke", [89, 91, 90, 88, 87, 92], "betty2024"],
    "daniel": [13, "Daniel Mulu", [86, 85, 88, 84, 87, 89], "dan_mulu"],
    "neima": [14, "Neima Abdurahman", [95, 96, 94, 92, 93, 91], "neima_pw"],
    "fikadu": [15, "Fikadu Wako", [76, 78, 79, 80, 75, 77], "fikadu_pw"],
    "samrawit": [16, "Samrawit Mekonnen", [88, 89, 90, 91, 87, 92], "samrawit92"],
    "yonas": [17, "Yonas Getachew", [84, 85, 86, 83, 87, 82], "yonas_82"],
    "aida": [18, "Aida Guta", [90, 92, 91, 93, 94, 95], "aida_pw"],
    "melat": [19, "Melat Eshetu", [78, 80, 77, 79, 81, 82], "melat78"],
    "nahom": [20, "Nahom Fekadu", [85, 83, 84, 82, 81, 86], "nahom_pw"],
    "abigail": [21, "Abigail Kidane", [91, 93, 92, 90, 89, 94], "abigail93"],
    "robel": [22, "Robel Gebre", [79, 80, 82, 81, 83, 78], "robel_pw"],
    "meron": [23, "Meron Habtamu", [86, 88, 87, 85, 89, 90], "meron_code"],
    "kaleb": [24, "Kaleb Zeleke", [73, 75, 74, 76, 72, 77], "kaleb_pw"],
    "abel": [25, "Abel Solomon", [94, 95, 93, 96, 92, 91], "abel_pw"]
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
def grade(a):
		if a>95:
			return "A+"
		elif a>90:
			return "A"
		elif a>86:
			return "A-"			
		elif a>80:
			return "B+"
		elif a>75:
			return "B"
		elif a>70:
			return "B-"
		else:
			return "D"					
def login():
		id=int(input("write your ID:   "))
		frist_name=input("write your fristname:  ")
		password=input("write your password:  ")
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
			print("english",english, grade(english))
			print('maths', maths, grade(maths))
			print("aptitude", aptitude,  grade(aptitude))
			print("chemistry",  chemistry,  grade(chemistry))
			print("pysics",pyesics, grade(pyesics))
			print("biology",biology,  grade(biology))
			print("total ", tota)
			print("average",ava)	
		else:
			print("\n\n")
			login()
		print("\n\n")	
		idea=input("you want to go for another session Y or N")
		if idea=="Y":
			print("\n\n\n\n")
			login()
					 
login()

