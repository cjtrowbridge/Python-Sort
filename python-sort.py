import random
import sys
import string


totalSize = 12000
totalSize = 11
ram = []*totalSize
bitlist = []

def displayAllRecords(ofWhat):
	i = 1
	while(i < len(ofWhat)):
		print(str(i)+":"+str(ofWhat[i]) + " "),
		i=i+1

def delete(set, byteNumber):
	set[byteNumber]='00000000'

def update(list, byteNumber,newValue):
	list[byteNumber]=newValue

def countValues(input, value):
	#count number of values in list
	values=0;
	i = 1
	while(i < len(input)):
		if str(input[i])=='{0:08b}'.format(int(value)):
			values = values+1
		i=i+1
	return values

def findBinaryMinimum(input,atLeast):
	atLeast=int(atLeast)
	print('looking for something >= than '+str(atLeast))
	i = 1
	min = int(input[i], 2)
	if(min<atLeast):
		min = atLeast
	while(i < len(input)):
		val = int(input[i], 2)
		if val < min and val > atLeast:
			min = val
		i=i+1
	min = '{0:08b}'.format(min)
	return min

def selectionSort(input):
	temp = input
	new = input
	position = 1
	values = len(input)-1
	lastMin=-1
	while position < values:
		min = findBinaryMinimum(temp,lastMin)
		lastMin = int(min)+1
		count = countValues(temp, min)
		print('minimum value of ' + str(min) + ' occurred ' + str(count) + ' times')
		#add that many to the new list and increment the position of the new list
		for x in range(count):
			update(new, position, min)
			position = position + 1
		print('im now at position '+str(position)+' of '+str(values))
	return new

def ppause():
	input('\nPress Enter to continue...')
	return 0
	

for x in range(totalSize):
	bitlist = []
	for i in range(0,8):
		x = str(random.randint(0,1))
		bitlist.append(x)
	bitstring = ''.join(bitlist)
	ram.append(bitstring)


#make one of the bytes blank just for testing purposes
delete(ram, 8)
	
print('Unsorted')
displayAllRecords(ram)


print('\nSelection Sorted')
selectionSorted = selectionSort(ram)
#displayAllRecords(selectionSorted)
