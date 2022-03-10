# Name: Blake Mann
# PSID: 1832387
import datetime
import time
months = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06", "July": "07", "August" : "08",
          "September": "09", "October": "10", "November": "11", "December": "12"}


input_dates = open('inputDates.txt', 'r')
output_date = open('parsedDates.txt', 'w')



def month_checker(string):
    flag = False
    listlet = (months.keys())
    for month in listlet:
        if string == month:
            flag = True
    return flag


def validtime(dates):
    today = str(datetime.datetime.today())
    today = today.split()
    todaycurr = today[0]
    x = todaycurr.replace('-', "")
    if int(x)-int(dates) <0:
        return False
    else:
        return True


def reformater(dates):
    date = time.strptime(dates, "%Y%m%d")
    date = time.strftime("%m/%d/%Y",date)
    return date




validD = []
for line in input_dates:
    if line != "-1":
        lis = line.split()
        if month_checker(lis[0]):
            month = lis[0]
            day = lis[1]
            year = lis[2]
            day = day.strip(",")
            if len(day)==1:
                day = "0"+day
            date = year+months[month]+day
            if validtime(date):
                validD.append(date)

for dvalue in validD:
    output_date.write(reformater(dvalue)+"\n")

output_date.close()

