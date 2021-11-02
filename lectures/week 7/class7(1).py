#Amaury Lendasse and Ed Ratner
#ID 007

#SLIDE 4
# my_list=[1,2,3]
# print(my_list[1])

#SLIDE 6
# my_list=['a','b','c','d','e']
# my_sublist=my_list[1:5]
# print(my_sublist)

#SLIDE 8
# my_list=[1,2,3,4,5,6,7,8]
# my_sublist=my_list[1:6:1]
# print(my_sublist)

#SLIDE 10
# my_list=['a','b','c','d']
# my_list.append('y')
# print(my_list)
# my_list.extend(['w','x'])
# print(my_list)
# my_list.insert(1,'z')
# print(my_list)

#SLIDE 12
# my_list=['a','b','c','d']
# my_list.remove('b')
# print(my_list)
# letter1=my_list.pop()
# print(letter1, my_list)
# letter2=my_list.pop(0)
# print(letter2, my_list)

#SLIDE 14
# my_list=['d',';','xa','x',',','DD','{','s']
# print(my_list)
# my_list.sort()
# print(my_list)
# my_list=[17,7,2,100]
# my_list.reverse()
# print(my_list)
# my_list.sort()
# print(my_list)

#SLIDE 16
# my_list=[1,2,3,2,5,2,2]
# print(my_list.index(2), my_list.count(2))

#SLIDE 18
# my_matrix = [ [23, 1,16], [98,43,12], [3, 4, 5]]
# print(my_matrix)
# x=my_matrix[1][2]   #note that it is 0 base!
# print(x)

#SLIDE 19
# my_matrix = [ [23, 1, 16], [98,43,12], [3, 4, 5]]
# for i in range(0,len(my_matrix)):
# 	print('Row',i)
# 	for j in range(0, len(my_matrix[0])):
# 		print(my_matrix[i][j])

#SLIDE 20
# my_table = [ [23, 1,16], [98,43,12,11,100], [3, 4, 5]] #unequal length
# sum=0
# for i in my_table:
# 	for j in i:
# 		sum+=j
# print(sum)

#SLIDE 22
# my_list = [3,4,5,6]
# new_list = [i**2+1 for i in my_list]
# print(new_list)

#SLIDE 24
# my_list=['x','b','z','a']
# def append_before_q(letter):
# 	return letter + ' is before q'
#
# new_list = [append_before_q(my_l) for my_l in my_list if my_l < 'q']
# for phrase in new_list:
# 	print(phrase)

#SLIDE 26
# import sys
# print(sys.argv[0])
# input_file = sys.argv[1]
# output_file =sys.argv[2]
# f=open(input_file,'r')
# f_out=open(output_file,'w')
# for line in f:
# 	f_out.write('here is '+line +'\n')  #should be lower case n for carriage return

