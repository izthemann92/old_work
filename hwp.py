# practice Blake Mann

months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
          "September": 9, "October": 10, "November": 11, "December": 12}
input_dates = open('inputDates.txt', 'r')

for line in input_dates:
    lis = line.split()
    if line.find(',') != -1:
        x = line.find(',')
        month = lis[0]


        print(months[month])
