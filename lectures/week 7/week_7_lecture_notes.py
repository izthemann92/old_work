# # Blake Mann
# # lecture notes
# # CHAPTER 10 CLASSES
# what is a  class?
# a class is a type of object that contains related variables and functions
# a way to group everything together
# provides for a straight forward way to extend functionality

# # class constructor
# class my_dictionary:
#     def __init__(self):
#         self.num_read = 0
#         self.dict = {}
# my_english_spanish = my_dictionary()
# print(my_english_spanish.dict)
# print(my_english_spanish.num_read)

# # how to add words into the dictionary using classes
#
# class my_dictionary:
#     def __init__(self):
#         self.num_read = 0
#         self.dict = {}
#     def set(self, word, translation):
#         self.dict[word] = translation
#     def read(self, word):
#         self.num_read+=1
#         return self.dict[word]
#
#
#
#
# my_english_spanish = my_dictionary()
# my_english_spanish.set('red', 'rojo')
# my_english_spanish.set('swimming pool', 'piscina')
# print(my_english_spanish.num_read)
# print(my_english_spanish.read('red'), my_english_spanish.num_read)
# print(my_english_spanish.read('red'), my_english_spanish.num_read)
# print(my_english_spanish.read('swimming pool'), my_english_spanish.num_read)

## stopped 42:21