#Name: Blake Mann
# PSID: 1832387

n = input()
lst = []
for x in n.split(" "):
    if int(x)>=0:
        lst.append(int(x))
lst.sort()
for x in lst:
    print(x,end=" ")

