# To print A P Q R
#          A B Q R
#          A B C R
#          A B C D

string1 = "ABCD"
string2 = "PQR"

for i in range(4):
     print(string1[0, i+1] + string2[i:])
