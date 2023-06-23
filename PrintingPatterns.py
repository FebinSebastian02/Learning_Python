# To print # # # #
#           # # #
#           # # #
#           # # #
print("First Pattern")
for i in range(4):
    for j in range(4):
        print("#", end="")
    print()

# To print #
#           #
#           # #
#           # # #

print("\nSecond Pattern")
for j in range(1, 5):
    print("# "*j)

# To print # # # #
#           # #
#           #

print("\nThird Pattern")
for i in range(4, 0, -1):
   print("# "*i)