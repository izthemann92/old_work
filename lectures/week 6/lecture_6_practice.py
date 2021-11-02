# Blake Mann
# week 6 lecture notes

# # STRINGS REVISITED
# # sets the stage for more complex objects
# # allows to see the operations intuitively

# # string slicing

# # my_substring = mystring[A:B]

# # A IS THE STARTING CHARACTER, B IS FIRST # # NOT INCLUDED # #

# # SLICING EXAMPLE
# my_string = 'this is my string'
# substring = my_string[5:7]
# substring1 = my_string[:5]
# substring2 = my_string[-6:]
# print(substring, substring1, substring2)
# print(substring2)

# # FIND AND REPLACE
# # FIND A SUBSTRING OR REPLACE A STRING BY ANOTHER ONE

# # LOC = MYSTRING.FIND(SUBSTRING) # # RETURNS INT FOR INDEX OR -1 IF NOT PRESENT

# # example
# my_string = 'this is my string'
# my_index = my_string.find('my')
# print(my_index)
# s_index = my_string.find('s', 4) # # 4 is the position where i start searching
# print(s_index) # # only prints the s location that is after the 4th position
# last_s_index = my_string.rfind('str')
# print(last_s_index)
# false_index = my_string.find('s', my_index, my_index+2)
# print(false_index)

# my_string = 'this is my string'
# new_string = my_string.replace('my', 'not my')
# print(new_string)

# # JOIN
# name1=input('What is the first person’s name? ')
# name2= input('What is the second person’s name? ')
# name3= input('What is the third person’s name? ')
# name4= input('What is the fourth person’s name? ')
# my_string = ' and '.join([name1, name2, name3, name4])
# print(my_string)

# # CHAPTER 9 FILES

# my_file=open('listofnames.txt','r') #format last name, first name
# for line in my_file:
# 	line=line.rstrip()
# 	name=line.split(',')
# 	print('First name is',name[1])
# 	print('Last name is',name[0])

# my_files = ['data1(1).txt', 'data2(1).txt', 'data3(1).txt']
# for file_name in my_files:
#     f = open(file_name, 'r')
#     print('in file', file_name)
#     for line in f:
#         line = line.rstrip()
#         print(line)
#     f.close()

# import csv
# file=open('mytext(1).txt','r')
# reader=csv.reader(file, delimiter=';')
# for line in reader:
#     print('This line has', len(line),'items')
# # 	# print(line)
#     print('The first item is',line[0])

