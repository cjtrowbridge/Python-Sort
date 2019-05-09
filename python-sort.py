import random
import sys
import string

byteSize = 8
byteCount = 1500

ram = []*(byteSize * byteCount)
bitlist = []

def displayAllRecords():
	i = 1
	while(i < len(ram)):
		print(str(i)+":"+str(ram[i]) + " "),
		i=i+1

def displayRecords(prepend =''):
	hundredth  = ''.join(str(v) for v in ram[99])
	thousandth = ''.join(str(v) for v in ram[999])
	print(prepend + 'hundredth element: '  + hundredth)
	print(prepend + 'thousandth element: ' + thousandth)

def update(byteNumber,newValue):
	ram[byteNumber]=newValue

for x in range(12000):
	bitlist = []
	for i in range(0,8):
		x = str(random.randint(0,1))
		bitlist.append(x)
	bitstring = ''.join(bitlist)
	ram.append(bitstring)
	
displayAllRecords()


