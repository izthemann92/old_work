#Blake Mann
# project 1
# PSID: 1832387
import csv

manlist = open('ManufacturerList.csv', mode='r') #open manufacturer list
pricelist = open('PriceList.csv', mode='r') #open pricelist
servicelist = open('ServiceDatesList.csv', mode='r') # open service dates list

# put manufacturer csv into a dictionary
with manlist as inp:
    reader = csv.reader(inp)
    manlistD = {rows[1]: rows[0:len(rows):] for rows in reader} # create a dictionary by serial number
# manlistD is dictionary

# sorted_mfl is a list
sorted_mflL = sorted(manlistD.items()) # sorting the dictionary by serial in ascending order
# # turned list into dictionary again
sorted_mflD = dict(sorted_mflL)
print(sorted_mflD)
print(type(sorted_mflD))


