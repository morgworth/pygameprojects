import random

def min3(num1, num2, num3):
	min=num1
	if num2<min:
		min=num2
		if num3<min:
			min=num3
	elif num3<min:
		min=num3
	
	return min

def box(h,w):
	for i in range(h):
		for j in range(w):
			print('*', end='')
		print()



def find(list, key):
	for i in range(len(list)):
		if list[i]==key:
			print('key ',key, ' found at index ', i)

def create_list(size):
	list=[]
	for i in range(size):
		list.append(random.randrange(1,7))	
	return list	

def count_list(list, key):
	count=0
	for num in list:
		if num==key:
			count+=1
	return count
	
def average_list(list):
	sum=0
	for num in list:
		sum+=num
	avg=sum/len(list)
	return avg
	
def main():
	print(min3(4, 7, 5))
	print(min3(4, 5, 5))
	print(min3(4, 4, 4))
	print(min3(-2, -6, -100))
	print(min3("Z", "B", "A"))
	
	box(7,5)  # Print a box 7 high, 5 across
	print()   # Blank line
	box(3,2)  # Print a box 3 high, 2 across
	print()   # Blank line
	box(3,10) # Print a box 3 high, 10 across
	
	my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
	find(my_list, 12)
	find(my_list, 91)
	find(my_list, 80)
	
	rand_list=create_list(5)
	print(rand_list)
	
	count = count_list([1,2,3,3,3,3,4,2,1],3)
	print(count)
	
	avg = average_list([1,1,1])
	print(avg)
	
	big_list=create_list(10000)
	print('1 occurs this many times: ', count_list(big_list,1))
	print('2 occurs this many times: ', count_list(big_list,2))
	print('3 occurs this many times: ', count_list(big_list,3))
	print('4 occurs this many times: ', count_list(big_list,4))
	print('5 occurs this many times: ', count_list(big_list,5))
	print('6 occurs this many times: ', count_list(big_list,6))
	print('The average of the list: ', average_list(big_list))

if __name__=='__main__':
	main()
