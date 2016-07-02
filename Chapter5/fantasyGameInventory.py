inventory = {'dust':3,'gold':5,'gauntlets':3}
def checkInv(inventory):
	print('Inventory items:')
	itemTotal=0
	for x,y in inventory.items():
		itemTotal+=y
		print(str(x)+': ' +str(y))
	print('Total items: ' +str(itemTotal))
