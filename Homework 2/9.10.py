# Name: Blake Mann
# PSID: 1832387

import csv
filename = input()
with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    result = dict()
    for x in reader:
        for i in x:
            if i in result:
                result[i] = result[i] + 1
            else:
                result[i] = 1
    for y in list(result.keys()):
        print("{} {}".format(y, result[y]))

