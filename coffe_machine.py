MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def coffe():
	while 2!=3:
		user=input("What would you like? (espresso/latte/cappuccino):")
		if user=="stop":
			break
		elif user=="report":
			print(resources)	
		else:
			if resources["water"]>=MENU[user]["ingredients"]["water"]:
				def cash():
					print("insert your pennies")
					pennies=int(input("how many pennies"))/100
					nickles=int(input("how many nicles"))/20
					dimes=int(input("how many dimes"))/10
					quarters=int(input("how many quartiles"))/4
					global money
					money=pennies + nickles  + dimes + quarters
				cash()	
				if money>MENU[user]["cost"]:
					back=money- float(MENU[user]["cost"])
					print("you can take", back, "£ away")
				elif money<MENU[user]["cost"]:
					left=MENU[user]["cost"]-money
					print("you have to add", left, "£ to these pennies and insert it")
					cash()
				else:
					print("enjoy your coffee")
					resources["water"]=resources["water"]-MENU[user]["ingredients"]["water"]
					resources["milk"]=resources["milk"]-MENU[user]["ingredients"]["milk"]
					resources["coffee"]=resources["coffee"]-MENU[user]["ingredients"]["coffee"]
					print("\n\n\n")
			else:
				print("not enough resources")
				refel=input("refeiling the resources")
				if refel=="kolaa":
					wata=int(input("how many ml of water"))
					milka=int(input("how many ml of milk"))
					coffa=int(input("how many g of coffee"))
					resources["coffee"]+=coffa
					resources["milk"]+=milka
					resources["water"]+=wata
					print("\n\n\n")				
coffe()				
					