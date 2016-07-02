#Chapter 5: checking inventory
#Author: Ricardo Laborde
#initialize dictionary
inventory = {'dust':3,'gold':5,'gauntlets':3}
def checkInv(inventory):
	print('Inventory items:')
	#initialize item total tally
	itemTotal=0
	#loop through the dictionary
	for x,y in inventory.items():
		#add value to total tally
		itemTotal+=y
		print(str(x)+': ' +str(y))
	print('Total items: ' +str(itemTotal))
