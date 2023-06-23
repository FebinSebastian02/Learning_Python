  # To print 1234
#            234
#            34
#            4

for i in range(1, 5):
    print(i, end=" ")
    for j in range(i,4):
        print(j+1, end=" ")
    print()