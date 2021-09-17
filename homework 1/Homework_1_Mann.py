# Blake Mann
# PSID: 1832387
print("Birthday Calculator")
month = int(input("Month: "))
Day = int(input("Day: "))
year = int(input("Year: "))
print("\nBirthday")
bmonth = int(input("Month: "))
bday = int(input("Day: "))
byear = int(input("Year: "))

age = year - byear
if (month == bmonth) and (Day == bday):
    print("Happy Birthday!!!")
    print("You are", age, "old")
elif month > bmonth and Day >= bday:
    age = age - 1
    print("You are", age, "years old")
elif month <= bmonth and Day >= bday:
    print("You are", age, "old")
