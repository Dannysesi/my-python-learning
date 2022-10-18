lst = []
for key, val in count.item():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=true)
print(lst)