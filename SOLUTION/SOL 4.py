# Python program to find the largest
# number among the three numbers

def maximum(a, b, c):

	if (a >= b) and (a >= c):
		largest = a

	elif (b >= a) and (b >= c):
		largest = b
	else:
		largest = c
		
	return largest


# Driven code
a=int(input("enter the number :"))
b=int(input("enter the number :"))
c=int(input("enter the number :"))
print('{0} is maximum number'.format (maximum(a, b, c)))
