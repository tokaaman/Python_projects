import random
cards=[
['A', 2, 3, 4, 5, 6, 7, 8, 9, 10,'J','K','Q'],
['A', 2, 3, 4, 5, 6, 7, 8, 9, 10,'J','K','Q'],
['A', 2, 3, 4, 5, 6, 7, 8, 9, 10,'J','K','Q'],
['A', 2, 3, 4, 5, 6, 7, 8, 9, 10,'J','K','Q']
]
def card_draw():
	a=random.randint(0,4)
	b=random.randint(0,13)
	return cards[a-1][b-1]
value={
'J':10,
'K':10,
'Q':10,
'A':11
}
for i in range(2,11):
	value[i]=i
def game():
	while 2!=3:
		start=input("do you want to start the game Y for yes and N for no")
		if start=="Y":
			def over(a,b):
				if a>21 and b<21:
					print("you loose")
				elif a<21 and b>21:
					print("you won")					
			def tie():
					print("it is a tie")
			def won(a,b):
				if a>b:
					print(f"your sum was {a} and computer was {b} you won")
				elif a==b:
					tie()
				else:
					print(f"your sum was {a} and computer was {b} you loose")
			def result(a,b):
				if a>21 or b>21:
					over(a,b)
				else:
					won(a,b)																	
			frist=card_draw()
			second=card_draw()
			sum=value[frist]+value[second]
			print(f"your cards are {frist} and {second} also the sum are  {sum}")
			frist_com=card_draw()
			second_com=card_draw()
			sum_com=value[frist_com]+value[second_com]
			print(f"the frist card of computer is {frist_com}")
			over(sum,sum_com)
			if sum==21 and sum_com!=21:
				print("you won")
				break
			elif sum_com==21 and sum==21:
				tie()
				break
			elif sum_com==21 and sum!=21:
				print("you loose")
				break
			else:
				if sum_com<17:
					another_com=card_draw()
					sum_com+=value[another_com]
				while 2!=4:
					idea=input("want to hit or stop")
					if idea=="hit":
						another=card_draw()
						sum+=value[another]
						if sum >=21:
							if another=="A":
								sum-=10
						print(f"you selected {another} and sum is {sum}")
						if sum==21 and sum_com!=21:
							print("you won")
							break
						elif sum!=21 and sum_com==21:
							print("you loose")
							break
						elif sum==21 and sum_com==21:
						      print("it is a tie")
						      break
						over(sum,sum_com)
						if over(sum,sum_com):
							break      
					else:
						     result(sum,sum_com)
						     print("\n\n")
						     break						     	
game()
		
	