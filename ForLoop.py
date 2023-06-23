list1 = [1, 2, 'Jiraiya']

#To print all values of list at once
print(list1)

#To print values of list one by one
for i in list1:
    print(i)

#To print values of a string one by one
string1 = "Pain"

for j in string1:
    print(j)

#To print value without assigning to a variable
for k in "Naruto":
    print(k)

#To print values from 11-20 with a difference of 2
for l in range(11, 21, 2):
    print(l)

#To print values from 11-20 in descending order
for m in range(20, 10, -1):
    print(m)

for n in range(1, 21):
    if n % 5 != 0:
        print(n)