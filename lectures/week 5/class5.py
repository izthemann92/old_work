#Amaury Lendasse and Ed Ratner
#ID 007


#SLIDE 5
# from math import sqrt
# def geometric_mean(a,b):
# 	geom_mean=sqrt(a*b)
# 	return geom_mean
# x=10
# y=100
# print('The geometric mean of',x,'and',y,'is',geometric_mean(x,y))


#SLIDE 6
# def square(i):
# 	return (i**2)
# def cube(i):
# 	return (i**3)
# List=range(2,100)
# List_squares=[]
# List_cubes=[]
# for i in List:
# 	List_squares.append(square(i))
# 	List_cubes.append(cube(i))
# print(List_squares)
# print(List_cubes)


#SLIDE 7
# from math import sqrt
# def both_means(a,b):
# 	geom_mean=sqrt(a*b)
# 	arith_mean=(a+b)/2.0
# 	return arith_mean,geom_mean
# x=7
# y=9
# a_mean,g_mean = both_means(x,y)
# print('The geometric mean of',x,'and',y,'is',g_mean)
# print('The arithmetic mean of',x,'and',y,'is',a_mean)

#SLIDE 10
# def compute_total_price(price_orange,number_orange,price_apple,number_apple):
# 	total=price_orange*number_orange+price_apple*number_apple
# 	return total
# Total_price=compute_total_price(price_apple=1.00,price_orange=0.50,number_apple=5,number_orange=8)
# print(Total_price)
# Total_price= compute_total_price(0.50, 8, number_apple=5,price_apple=1.0)
# print(Total_price)
# Total_price= compute_total_price(0.50, 8, 1.0, 5)
# print(Total_price)


#SLIDE 12
# def compute_total_price(number_orange, number_apple, price_orange=0.75, price_apple=1.25):
# 	total=price_orange*number_orange+price_apple*number_apple
# 	return total
# Total_price= compute_total_price(10, 8, 1.0, 0.5) #set both prices
# print(Total_price)
# Total_price= compute_total_price(10, 8)  #use just number of items
# print(Total_price)
# Total_price= compute_total_price(10, 8, 1.0)  #set price of oranges
# print(Total_price)
# Total_price= compute_total_price(10, 8, price_apple=1.00) #set both prices
# print(Total_price)



#SLIDE 14
# def sum_of_squares(my_object):
# 	sum=0
# 	for i in my_object:
# 		sum+=i**2
# 	return sum
#
# My_list=range(4,99,7)
# My_list=range(1,4)
# List_sum=sum_of_squares(My_list)
# print(List_sum)
# My_set={9,45,39,786}
# Set_sum=sum_of_squares(My_set)
# print(Set_sum)


#SLIDE 17
# def print_my_friend(*args):
# 	for name in args:
# 		print(name,'is my friend')
# print_my_friend('Bob', 'Alice')
# print_my_friend('Eric')
# print_my_friend('Bob', 'Peggy','John','Enrique','Victor')


#SLIDE 18
# def print_my_friend(args):
# 	for name in args:
# 		print(name,'is my friend')
# My_list=['Bob', 'Alice']
# print_my_friend(My_list)


#SLIDE 20
# def print_location(document,*args,**kwargs):
# 	print('The main documents is', document)
# 	if len(args)>0:
# 		print('The additional documents are:')
# 		for doc in args:
# 			print(doc)
# 	for loc_type, address in kwargs.items():
# 		if (loc_type=='file'):
# 			print('The file name is', address)
# 		elif (loc_type=='url'):
# 			print('The web location is', address)
# 		else:
# 			print('Find these here',loc_type,address)
#
# print_location('ccc.txt','ddd.txt','eee.txt',file='fff.txt',url='www.uh.edu',other='what else?')


#SLIDE 23
# def total_price(num_oranges):
# 	return num_oranges*price_orange
# price_orange=0.80
# print (total_price(6), price_orange)


#SLIDE 24
# def total_price(num_oranges):
# 	global price_orange
# 	if price_orange<1.0:
# 		price_orange=1.0
# 	return num_oranges*price_orange
# price_orange=0.80
# print (total_price(6), price_orange)


#SLIDE 26
# def total_price(num_oranges, price_orange):
# 	if price_orange<1.0:
# 		price_orange=1.0
# 	return num_oranges*price_orange, price_orange
# price_orange=0.80
# Total, price_orange =total_price(6,price_orange)
# print (Total, price_orange)


#SLIDE 27
def add(a,b):
		return a+b
def multiply(a,b):
		return (a*b)
def operate(operation,a,b):
		return operation(a,b)

# print(operate(add,8,9))
print(operate(multiply,6,5))
