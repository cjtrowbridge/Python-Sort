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

def update(byteNumber,newValue):
	ram[byteNumber]=newValue

for x in range(totalSize):
	bitlist = []
	for i in range(0,8):
		x = str(random.randint(0,1))
		bitlist.append(x)
	bitstring = ''.join(bitlist)
	ram.append(bitstring)

def countValues(input, value):
	#count number of values in list
	values=0;
	i = 1
	while(i < len(input)):
		if str(input[i])=='00000000':
			values = values+1
		i=i+1
	
	return values

def findBinaryMinimum(input):
	i = 1
	min = int(input[i], 2)
	while(i < len(input)):
		val = int(input[i], 2)
		if val < min:
			min = val
		i=i+1
	return min

def selectionSort(input):
	new=[]*len(input)
	
	min = findBinaryMinimum(input)
	count = countValues(input, min)
	print('minimum value of ' + str(min) + ' occurred ' + str(count) + ' times')
	
	#for x in range(values):
	#	new.append('000000')
	
	return new


delete(ram, 8)
	
print('Unsorted')
displayAllRecords(ram)

print('\n')
print('Selection Sorted')
selectionSorted = selectionSort(ram)
displayAllRecords(selectionSorted)


