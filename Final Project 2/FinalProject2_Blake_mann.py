# # Blake Mann
# # PSID: 1832387

import csv
from datetime import datetime

strp = datetime.strptime
# assigning the list variables
manL = 'FinalProjectManufacturerList.csv'
priceL = 'FinalProjectPriceList.csv'
serviceD = 'FinalProjectServiceDatesList.csv'

# opening all files and putting them in a tuple
with open(manL, newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]
with open(priceL, newline='') as g:
    reader = csv.reader(g)
    pdata = [tuple(row) for row in reader]
with open(serviceD, newline='') as h:
    reader = csv.reader(h)
    sdata = [tuple(row) for row in reader]

new_list = []
for x in range(len(data)):
    for row in pdata:
        if row[0] in data[x]:
            xyz = list(data[x])

            xyz.append(row[1])

            new_list.append(row[1])
            data[x] = tuple(xyz)

## adding service list dates to the end of the master file
new_list2 = []
for x in range(len(data)):
    for row in sdata:
        if row[0] in data[x]:
            xyz = list(data[x])
            xyz.append(row[1])
            data[x] = tuple(xyz)

mdata = []
## arranging the list in the desired order
for x in range(len(data)):
    for row in data:
        xyz = list(data[x])
        temp = xyz[3]
        date = xyz[5]
        price = xyz[4]
        xyz[4] = date
        xyz[5] = temp
        xyz[3] = price
        data[x] = tuple(xyz)


# creating a function to write the list correctly and output correct format

def formatter(listlet):
    stringlet = ""
    for k in listlet:
        for i in k:
            if i == "" or i == "damaged":             # had to go through and look for damaged so it would out put correctly
                stringlet = stringlet + i
            else:
                stringlet = stringlet + i + ","

        stringlet += "\n"

    return stringlet


# create laptop list
laptoplist = []
for x in range(len(data)):

    if data[x][2] == "laptop":
        listlet = list(data[x])
        laptoplist.append(listlet)

# create damage inventory
damage = []
for x in range(len(data)):
    if data[x][5] == 'damaged':
        listlet = list(data[x])
        damage.append(listlet)

# remove the word damaged in the list
for x in range(len(damage)):
    if damage[x][5] == 'damaged':
        del damage[x][5]

# create past dates list
exp_serv = []
for x in range(len(data)):
    listlet = list(data[x])
    service = listlet[4]
    today = datetime.now().date()
    serv_exp = datetime.strptime(service, "%m/%d/%Y").date()
    if serv_exp < today:
        exp_serv.append(listlet)


# create a function to order my brand
def brand(item):
    return item[1]


# create a function to order them by id
def manid(item):
    return item[0]


# created a function to order by price
def itemprice(item):
    return item[3]


# create a function to order by date
def dateorder(item):
    return item[4]


# writing all new list to the desired csv
finalFull = 'FinalProjectFullInventory.csv'
with open(finalFull, 'w') as j:
    j.write(formatter(sorted(data, key=brand)))

## -------------------- PART 2 ------------------------------

with open(finalFull, newline='') as f:
    reader = csv.reader(f)
    final_full2 = [tuple(row) for row in reader]


item_q = input('\nEnter a query for an item by searching Manufacturer and item type or press \'q\' to exit: ')
item_c = []

man1 = [] # used to store manufacturer
item1 = [] # used to store the specific item
selection = [] # if an row in final list matches the above variables it is stored here
exp_date = [] # needed a empty set for expiration dates
dmg = [] #
extra = []
past = []
also = []
while item_q != 'q':

    p = item_q.split(' ')

    # creating a for loop to use the query to find matches and store those matches in item_c
    for i in range(0, len(p)):
        for row in final_full2:
            if p[i] in row:
                item_c.append(row)
                # possible matches will be stored in item_c
    for x in range(len(item_c)):
        xyz = list(item_c[x])

        for i in range(len(p)):

            if p[i] == xyz[1]:
                ## storing the manufacturer in man1
                man1.append(p[i])


            elif p[i] == xyz[2]:
                ## sorting the item type in item1
                item1.append(p[i])


    # added if statement to correct index error
    if not item1:
        item1 = 'extra'
    elif not man1:
        man1 = 'extra'

    item1 = list(dict.fromkeys(item1))
    man1 = list(dict.fromkeys(man1))

    for y in range(len(item_c)):
        abc = list(item_c[y])

        if man1[0] in abc and item1[0] in abc:
            selection.append(item_c[y])                  #keeping the selection if manufacturer and item found a match

    final_selection = list(dict.fromkeys(selection))


    def sort_tup(final_selection):
        return sorted(final_selection, key=lambda l: l[3], reverse = True)

    final_selection2 = sorted(final_selection, key = lambda x :x[3], reverse = True)

    for i in range(len(final_selection2)):
        xyz = list(final_selection2[i])
        today = datetime.now().date()
        service = xyz[4]
        past_service = datetime.strptime(service, '%m/%d/%Y').date()
        temp = xyz[3]
        if not final_selection2:
            print('No such item in inventory')
        elif xyz[5] == 'damaged':
            dmg.append(final_selection2[i])

        elif past_service < today:
            past.append(final_selection2[i])

        elif len(final_selection2) > 1:
            extra.append(final_selection2[i])



    if not extra:
        print('No such item in inventory')
        extra = ['none']
    else:
        print('Your item is:', extra[0])
    ## looking for suggestions if any available


    for c in range(0, len(final_full2)):
        xyz = list(final_full2[c])
        today = datetime.now().date()
        service = xyz[4]
        past_service = datetime.strptime(service, '%m/%d/%Y').date()

        if xyz[5] == 'damaged':
            dmg.append(final_full2[c])
        elif past_service < today:
            past.append(final_full2[c])
        elif item1[0] in final_full2[c] and final_full2[c] != extra[0]: # raising index error if item1 was empty
            also.append(final_full2[c])
        else:
            pass

    if not also:
        pass
    else:
        print('You may also, consider: e', also[0])
    # used to reset all of the lists i created
    man1 = []
    item1 = []
    selection = []
    exp_date = []
    dmg = []
    extra = []
    past = []
    also = []
    item_q = input('\nEnter a query for an item by searching Manufacturer and item type or press \'q\' to exit: ')


