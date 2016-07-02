#Chapter 5: Part Two Programming challenge
#Adding items to dictionary and displaying count of items
#Author: Ricardo Laborde
inventory = {'dust':3,'gold':5,'gauntlets':3}
loot=['gold','gold','gold','gauntlets','paper']

def addToInventory(inventory,loot):
	#loop through every item in  loot list
	for i in range(len(loot)):
		#this adds the item if it does not exist in the current inventory dictionary
		inventory.setdefault(loot[i],0)
		#adds the int value to the dictionary key
		inventory[loot[i]]=inventory[loot[i]]+1
	return inventory
	
def checkInv(inventory):
	print('Inventory items:')
	#initialize the item total count
	itemTotal=0
	#loop through the inventory dictionary, key=x value=y
	for x,y in inventory.items():
		#add the value to the item total tally
		itemTotal+=y
		print(str(x)+': ' +str(y))
	print('Total items: ' +str(itemTotal))

#check initial inventory
checkInv(inventory)
#add list items to dictionary
addToInventory(inventory,loot)
#display the inventory after list items have been added
checkInv(inventory)
