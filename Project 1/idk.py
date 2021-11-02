new_list = [('Germany',120), ('France',110) , ('England',40) , ('Japan',184), ('China',20)]

new_ele = 0
new_lis_len = len(new_list)
for k in range(0, new_lis_len):
    for l in range(0, new_lis_len-k-1):
        if (new_list[l][new_ele] > new_list[l + 1][new_ele]):
            new_tem = new_list[l]
            new_list[l]= new_list[l + 1]
            new_list[l + 1]= new_tem

print(new_list)