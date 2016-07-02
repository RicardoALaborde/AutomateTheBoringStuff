inventory = {'dust':3,'gold':5,'gauntlets':3}
loot=['gold','gold','gold','gauntlets','paper']

def addToInventory(inventory,loot):
	itemTotal=0
	for i in range(len(loot)):
		inventory.setdefault(loot[i],0)
		inventory[loot[i]]=inventory[loot[i]]+1
	return inventory
	
def checkInv(inventory):
	print('Inventory items:')
	itemTotal=0
	for x,y in inventory.items():
		itemTotal+=y
		print(str(x)+': ' +str(y))
	print('Total items: ' +str(itemTotal))

checkInv(inventory)
addToInventory(inventory,loot)
checkInv(inventory)
