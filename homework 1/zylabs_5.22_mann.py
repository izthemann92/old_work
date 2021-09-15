# Name: Blake Mann
# PSID: 1832387
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")
services_dict = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12,
    "-": 0
}

ser1 = input("Select first service:\n")
ser2 = input("Select second service:\n")
print("\nDavy's auto shop invoice\n")
if ser1 == "-":
    print("Service 1: No service")
else:
    print("Service 1: {:s}, ${:d}".format(ser1, services_dict.get(ser1)))
if ser2 == "-":
    print("Service 2: No service")
else:
    print("Service 2: {:s}, ${:d}".format(ser2, services_dict.get(ser2)))

print("\nTotal:", "${}".format(services_dict[ser1] + services_dict[ser2]))
