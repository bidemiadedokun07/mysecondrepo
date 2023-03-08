# This is the sript for python self practice 
## this program will run a coffee transaction 

print("\nWelcome to the Bmic Coffe shop, we are always happy to serve you \nWhat do you want to buy? \n")
product = input("Enter Coffee, Snack, or Water here: ")

product = product.upper()
promo_val = 30
if product == 'COFFEE':
	cof_cream = input("Input Yes or No, Do you want Cream?: ")
	cof_size = input("Small, Regular, or Large?: ")
	cof_promo = input("Type Yes or No, Do you have promo code?: ")
	if cof_promo.lower() == "yes":
		print("You have {}/% discount on any of our product:".format(promo_val))
	# Coffee Price 
	if cof_size.lower() == "small":
		coffee_price = 2.59
	elif cof_size.lower() == "regular":
		coffee_price = 3.99
	elif cof_size.lower() == "large":
		coffee_price = 4.99
	else:
		print("\nWe might not be able to help you with that") 
	
	# Payment mode
	cof_payment = input("Cash or Card?: ")
	if cof_payment.lower() == "cash" :
		print("\nSince you are paying with cash, your denomination can be 5, 10, 20, or 100 Dollars\n")
		cash_deno = int(input("Enter the denomination you are paying: "))
		
		if cof_promo.lower() == "yes":
			change = cash_deno -  (promo_val/100)*coffee_price
		else:
			change = cash_deno - coffee_price
	else:
		print("\n Sorry!, we only do cash") 
print("Your change is {}" .format(change))

print("Thank you for transacting with us. we love to have you arround")

print()
