dictionary=[3,4,5,6,7,8,2,3,4,5]

duplicateitem = set()
uniqueitem = []
for x in dictionary:
    if x not in duplicateitem:
        uniqueitem.append(x)
        duplicateitem.add(x)

print(duplicateitem)