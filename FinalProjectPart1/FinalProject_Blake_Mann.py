# # Blake Mann
# # PSID: 1832387

import csv
from datetime import datetime

strp = datetime.strptime
# assigning the list variables
manL = 'FinalProjectInputManufacturerList.csv'
priceL = 'FinalProjectInputPriceList.csv'
serviceD = 'FinalProjectInputServiceDatesList4.csv'

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
        # if temp == 'damaged':
        xyz[4] = date
        xyz[5] = temp
        xyz[3] = price
        data[x] = tuple(xyz)


# creating a function to write the list correctly and output correct format

def formatter(listlet):
    stringlet = ""
    for k in listlet:
        for i in k:
            if i == "" or i == "damaged": # had to go through and look for damaged so it would out put correctly
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
finalFull = '1FinalProjectFullInventory.csv'
with open(finalFull, 'w') as j:
    j.write(formatter(sorted(data, key=brand)))

finalLaptop = '1FinalProjectLaptopInventory.csv'
with open(finalLaptop, 'w') as g:
    g.write(formatter(sorted(laptoplist, key=manid)))
finalexp = '1FinalProjectPastServiceDateInventory.csv'
with open(finalexp, 'w') as f:
    f.write(formatter(sorted(exp_serv, key=lambda sub: strp(sub[4], "%m/%d/%Y"))))

finalDamage = '1FinalProjectDamagedInventory.csv'
with open(finalDamage, 'w') as h:
    h.write(formatter(sorted(damage, key=itemprice, reverse=True)))



#should produce new files with 2 in front of them

# sorry 1
