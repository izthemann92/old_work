#Amaury Lendasse and Ed Ratner
#ID 007

#SLIDE 5
# my_string='this is my string'
# substring=my_string[5:7]
# substring1=my_string[:5]
# substring2=my_string[-6:]
# print(substring, substring1, substring2)
# print(substring2)

#SLIDE 7
# my_string='this is my string'
# my_index=my_string.find('my')
# # print(my_index)
# s_index=my_string.find('s',4)
# # print(s_index)
# last_s_index=my_string.rfind('str')
# # print(last_s_index)
# false_index=my_string.find('s',my_index,my_index+2)
# print(false_index)
# print(my_index, s_index, last_s_index, false_index)

#SLIDE 8
# my_string='this is my string'
# new_string=my_string.replace('my', 'not my')
# print(new_string)

#SLIDE 9
# my_string='This is my string'
# number=my_string.count('s')
# print(number)
# number2=my_string.count('t')
# print(number2)
# number3=my_string.count('w')
# print(number3)

#SLIDE 11
# my_phone='865-723-2222'
# my_list=my_phone.split('-')
# my_area_code=my_list[0]
# print(my_list, my_area_code)

#SLIDE 12
# name1=input('What is the first person’s name? ')
# name2= input('What is the second person’s name? ')
# name3= input('What is the third person’s name? ')
# name4= input('What is the fourth person’s name? ')
# my_string=' and '.join([name1,name2,name3,name4])
# print(my_string)

#SLIDE 17
# my_file=open('data.txt','r')
# file_contents=my_file.read() #reads all the data into a single string
# print(file_contents)

#SLIDE 19
# my_file=open('listofnames.txt','r') #format last name, first name
# for line in my_file:
# 	line=line.rstrip()
# 	name=line.split(',')
# 	print('First name is',name[1])
# 	print('Last name is',name[0])

#SLIDE 23
# my_files=['data1.txt','data2.txt','data3.txt']
# for file_name in my_files:
# 	f=open(file_name,'r')
# 	print('in file', file_name)
# 	for line in f:
# 		line = line.rstrip()
# 		print(line)
# 	f.close()

# SLIDE 27
# my_files=['data1.txt','data2.txt','data3.txt']
# for file_name in my_files:
# 	with open(file_name,'r') as f:
# 		print('in file', file_name)
# 		for line in f:
# 			line = line.rstrip()
# 			print(line)

#SLIDE 31
# import csv
# file=open('mytext.txt','r')
# reader=csv.reader(file, delimiter=';')
# for line in reader:
#     print('This line has', len(line),'items')
# # 	# print(line)
#     print('The first item is',line[0])