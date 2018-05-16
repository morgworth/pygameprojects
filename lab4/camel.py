import random

print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive your')
print('desert trek and out run the natives.')

done=False
miles=0
thirst=0
fatigue=0
nativeMiles=-20
numDrinks=3

while done==False:
	print()
	print('A. Drink from your canteen.')
	print('B. Ahead moderate speed.')
	print('C. Ahead full speed.')
	print('D. Stop for the night.')
	print('E. Status check.')
	print('Q. Quit.')
	
	choice=input('What do you choose? ')
	if choice.upper()=='Q':
		done=True
	elif choice.upper()=='E':
		print('Miles traveled: ',miles)
		print('Drinks in canteen: ',numDrinks)
		print('The natives are ', miles-nativeMiles, ' miles behind you.')
	elif choice.upper()=='D':
		fatigue=0
		nativeMiles+=random.randrange(7,15)
		print('The camel is well-rested, happy, and ready to go!')
	elif choice.upper()=='C':
		miles+=random.randrange(10,21)
		print('You have travelled ', miles, ' miles.')
		thirst+=1
		fatigue+=random.randrange(1,4)
		nativeMiles+=random.randrange(7,15)
	elif choice.upper()=='B':
		miles+=random.randrange(5,13)
		print('You have travelled ', miles, ' miles.')
		thirst+=1
		fatigue+=1
		nativeMiles+=random.randrange(7,15)
	elif choice.upper()=='A':
		if numDrinks>0:
			numDrinks-=1
			thirst=0
		else:
			print('Nothing but dust out here.')
	
	if thirst > 6:
		print('You died of thirst.')
		done=True
	elif thirst > 4:
		print('You are thirsty.')
		
	if not done:
		if fatigue > 8:
			print('The camel died of fatigue.')
			done=True
		elif fatigue > 5:
			print('The camel is getting tired.')

	if not done:
		if miles-nativeMiles <= 0:
			print('The natives caught you. Beg for forgiveness.')
			done=True
		elif miles-nativeMiles < 15:
			print('The natives are getting close!')
	
	if not done and miles >= 200:
		print('You have crossed the desert and successfully gotten away! Good camel thief.')
		done=True
	
	oasisChance=random.randrange(1,21)
	if not done and oasisChance == 15:
		print('You have found an oasis. Fully restored.')
		numDrinks=3
		fatigue=0
		thirst=0
