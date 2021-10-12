#Amaury Lendasse and Ed Ratner
#ID 007

#SLIDE 6
# x=0                                  #initializes the variable outside the loop
# while x<4:                       #the conditional expression contains the loop variable
#     print(x)
#     x=x+1

#SLIDE 7
# print square roots, -1 exits
# import math
# x=0
# while x!=-1:
# 	if (x!=0):
# 		print('the square root is', math.sqrt(x))
# 	x=int(input('Type your whole number '))

#SLIDE 8
# print the first N perfect squares
# import time
# N=77
# i=0
# while i<N:
#     i+=1
#     print(i**2)
#     time.sleep(0.250)

#SLIDE 9
# #print the first N perfect squares
# import time
# N=77
# i=1
# while i < N+1:
#     print(i**2)
#     i+=1
#     time.sleep(0.250)

#SLIDE 12
# name_list =['Bob', 'Alice', 'John']
# for name in name_list:
# 	print('the name is',name)
# 	l=name[0]
# 	print('the first letter of', name, ' is ', l)

# SLIDE 13
# name_list = ['Bob', 'Alice', 'John']
# for name in reversed(name_list):
#     print('the name is', name)
#     l = name[0]
#     print('the first letter of', name, ' is ', l)

# SLIDE 14
# name_set ={'Bob', 'Alice', 'John'}
# for name in name_set:
# 	print('the name is',name)
# 	l=name[0]
# 	print('the first letter of ', name, ' is ', l)

# SLIDE 16
# for i in range(10, -10,-1):
# 	if ( i%3 == 0 ):
# 		print(i, 'is divisible by 3')

# SLIDE 17
# flavor_type =['cherry', 'apple', 'peach']
# dessert_type =['pie', 'cobbler']
# for flavor in flavor_type:
#     for dessert in dessert_type:
#         print('I like',flavor, dessert)

# SLIDE 19
# for (index, i) in enumerate(range(-7, -199, -22)):
# 	print('the element is', i)
# 	size_of_list=len(range(-7, -199, -22))
# 	percentile=(index+1)/size_of_list*100.00
# 	print('we are ', round(percentile,2), '% through our task',sep='')

# SLIDE 19bis
# myrange = range(-7, -199, -22)
# size_of_list=len(myrange)
# for (index, i) in enumerate(myrange):
# 	print('the element is', i)
# 	percentile=(index+1)/size_of_list*100.00
# 	print('we are ', round(percentile,2), '% through our task',sep='')

# SLIDE 21
# friends_list=['Peggy','Enrique','Ed','Tammy']
# for name in friends_list:
# 	if name=='Enrique':
# 		continue
# 	print('I like',name)
# print('All done')

# SLIDE 22
# friends_list=['Alice','Bob','Joe','Tammy']
# for name in friends_list:
# 	if name=='Bob':
# 		break
# 	print('I like',name)
# print('All done')

# SLIDE 23
# while 1>0:
# 	number=int(input('Tell me your number, -1 to exit '))
# 	print(number)
# 	if number==-1:
# 		break

# SLIDE 24
# number=0
# while number != -1:
# 	number=int(input('Tell me your number, -1 to exit '))
# 	print(number)

# SLIDE 25
# friends_list=['Alice','Bob','Joe','Tammy']
# for name in friends_list:
# 	if name=='Bob':
# 		break
# 	print('I like',name)
# else:
# 	print('All done')

# SLIDE 26
i=10
while i>0:
	name = input('Pick a name, type Q to quit ')
	if name=='Q':
		break
	print('Your choice is',name)
	i-=1
else:
	print('completed 10 names')

