# Name: Blake Mann
# PSID: 1832387

# a

months_list = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
               "September": 9, "October": 10, "November": 11, "December": 12}
input_dates = open("inputDates.txt", 'r')
output_dates = open("parsedDates.txt", 'w')

for line in input_dates:
    if line != "-1":
        lis = line.split()

        if len(lis) >= 3:
            month = lis[0]
            day = lis[1]
            year = lis[2]
            print(months_list[month],day, year)
