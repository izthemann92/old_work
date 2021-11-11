# Name: Blake Mann
# PSID: 1832387
# Homework 11.22 word frequencies

w = input()
wlst = w.split()
lst = []


for w in wlst:
    c = wlst.count(w)
    n = wlst[wlst.index(w)]
    print('{} {}'.format(n, c))










