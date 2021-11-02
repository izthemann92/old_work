import csv

manlist = open('ManufacturerList.csv', mode='r')

with manlist as inp:
    reader = csv.reader(inp)
    manlistD = {rows[0]:rows[1] for rows in reader}

print(manlistD)