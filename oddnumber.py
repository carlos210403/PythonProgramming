# Programmer : Carlos Suarez
# Program : Odd Numbers
# First Created : 09/21/2022 08:20:00
# Last Changed :  09/21/2022 11:32:00
# Version : 3.7.9

# print("Printing Odd Number from First 100 Natural Numbers")
#
# for i in range (0, 101):
#     if (i%2 != 0):
#         print(i, end=' ')
#
# print("Alternate Approach")
# for k in range(1, 51):
#     print(((2*k)-1), end=' ')

print("Printing Odd Number from First 100 Naturals Numbers while using loop")
i=1
while i <= 100:
    if i%2!=0:
        print(i, end=' ')
    i=i+1
