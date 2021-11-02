# Blake Mann
# lecture 5 video recording

# # why do we need functions ?
# # answer: when you have to code the same thing several times.
# when are functions useful

# simple function example

# from math import sqrt
#
#
# def geometric_mean(A, B):
#     geom_mean = sqrt(A * B)
#     return geom_mean
#
#
# x = 7
# y = 9
# print('The geometric mean of ', x, 'and', y, 'is', geometric_mean(x, y))

# # for readability write code in a modular way

# def square(i):
#     return (i**2)
# def cube(i):
#     return(i**3)
# list = range(2,100)
# list_squares = []
# list_cubes = []
# for i in list:
#     list_squares.append(square(i))
#     list_cubes.append(cube(i))
#
# print(list_squares)
# print(list_cubes)

# multiple returns

# from math import sqrt
#
#
# def both_means(A, B):
#     geom_mean = sqrt(A * B)
#     arith_mean = (A + B) / 2.0
#     return arith_mean, geom_mean # these functions have to be presented in the same way they are presented
#
#
#
# x = 7
# y = 9
#
# a_mean, g_mean = both_means(x, y)
# print('THE SUM OF THE GEOMETRIC AND ARITHMETIC MEANS OF', x, 'AND', y, 'IS', a_mean + g_mean)
# print('The geometric mean of',x,'and',y,'is',g_mean)
# print('The arithmetic mean of',x,'and',y,'is',a_mean)

# # we use multiple returns

# # when you want to make it very clear which individual variables are set by the function

# # when the number of returns is small
# #  when the number of return values is fixed

# # PASSING ARGUMENTS BY KEYWORDS

# def compute_total_price(price_orange, number_orange, price_apple, number_apple):
#     total = price_orange * number_orange + price_apple * number_apple
#     return total
#
#
# total_price = compute_total_price(price_apple=1.00, price_orange=.50, number_apple=5, number_orange=8)
# print(total_price)
# total_price = compute_total_price(.50,8,number_apple=5, price_apple=1.0)
# print(total_price)
# total_price = compute_total_price(.50,8,1.0,5) # # you can simply put the amount but have to keep track of the order
#                                                # # in which the variables are used in the function.
# print(total_price)

# SLIDE 12
# def compute_total_price(number_orange, number_apple, price_orange=0.75, price_apple=1.25):
# 	total=price_orange*number_orange+price_apple*number_apple
# 	return total
#
# Total_price= compute_total_price(10, 8, 1.0, 0.5) #set both prices
# print(Total_price)
# Total_price= compute_total_price(10, 8)  #use just number of items
# print(Total_price)
# Total_price= compute_total_price(10, 8, 1.0)  #set price of oranges
# print(Total_price)
# Total_price= compute_total_price(10, 8, price_apple=1.00) #set both prices
# print(Total_price)
#
# Total_price = compute_total_price(10,8,1.0)
# # # when you do not specify the value it takes the default value
# print(Total_price)

# #  OBJECTS CAN BE USED AS ARGUMENTS
# # LISTS, DICTIONARIES, AND SETS MAY BE ALL USED AS PARAMETERS OF A FUNCTION

# def sum_of_squares(my_object):
# 	SUM = 0
# 	for i in my_object:
# 		SUM+= i ** 2
# 	return SUM
# my_list = range(4,99,7)
# list_sum = sum_of_squares(my_list)
# print(list_sum)
# my_set = {9,45,39,786}
# set_sum = sum_of_squares(my_set)
# print(set_sum)

# # BREAK SLEEP TIME COME BACK 51:441


# # FUNCTIONS WITH FLEXIBLE NUMBER OF PARAMETERS

# # USE *ARGS TO DEFINE A FUNCTION WHERE THE NUMBER OF PARAMETERS IS FLEXIBLE
# # WILL PUT THE CORRESPONDING PARAMETERS IN A LIST
# # FUNCTION CAN PROCESS THE LIST
# # ALLOWS FOR GREATER FLEXIBILITY AND CLEARER VIEW OF WHAT IS PASSED IN

# def print_my_friend(*args):
#     for name in args:
#         print(name,'is my friend')
#
# print_my_friend('Bob', 'Alice')
# print_my_friend('Eric')
# print_my_friend('Bob', 'Peggy','John','Enrique','Victor')
# # # *args collects all of the elements

# # USING ARGS ONLY

# def print_my_friends(args):
#     for name in args:
#         print(name,'is my friend')
# my_list = ["Bob", "Alice"]
# print_my_friends(my_list)

# # **KWARGS IS A WAY TO PROVIDE KEYWORDS TO THE FUNCTION
# # IT IS ALWAYS THE LAST PARAMETER OF A FUNCTION


# def print_friends(document, *args, **kwargs):
#     print('the main document is', document)
#     if len(args) > 0:
#         print('the additional documents are:')
#         for doc in args:  # # the *args is used to gather all the additional elements
#             print(doc)
#     for loc_type, address in kwargs.items():  # # **kwargs was used to use keywords
#         if loc_type == 'file':
#             print('the file name is', address)
#         elif loc_type == 'url':
#             print('the web location is', address)
#         else:
#             print('find these here', loc_type, address)
#
#
# print_friends('ccc.txt', 'ddd.txt', 'eee.txt', file='fff.txt', url='www.uh.edu', other='what else?')
# # # *args                          # # **kwargs

# # VARIABLE SCOPE


# # VARIABLE CAN BE DEFINED GLOBALLY OR LOCALLY

# # LOCAL VARIABLES CAN HAVE SAME NAMES AS GLOBAL VARIABLES
# # GLOBAL VARIABLES ARE AVAILABLE TO ALL FUNCTIONS

## LOCAL VARIABLES NOT AVAILABLE OUTSIDE (EXAMPLE)

# # GLOBAL VARIABLES
# # bad coding
# def total_price(num_oranges):
#     return num_oranges*price_orange
# price_orange = 0.80
# print(total_price(6), price_orange)

## bad coding
# def total_price(num_oranges):
#     global price_orange
#     if price_orange<1.0:
#         price_orange = 1.0 # # changing the variable in the function will change it globally.
#     return num_oranges*price_orange
# price_orange = 0.80
# print(total_price(6), price_orange)

def total_price(num_oranges, price_orange):
    if price_orange < 1.0:
        price_orange = 1.0
    return num_oranges*price_orange, price_orange
price_orange = 0.80
total, price_orange = total_price(6, price_orange)
print(total, price_orange)