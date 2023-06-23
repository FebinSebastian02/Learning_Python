# To print first divisible number by 5 in a list

list1 = [11, 13, 15, 17, 19, 21]

for i in list1:
    if i % 5 == 0:
        print(i)
        break
else:
    print("Nothing found")