#Leap Year
#x here is representative of a year
x=2025
if (x % 400 == 0):
    print('True')
elif (x % 4 ==0) and (x % 100 != 0):
    print('True')
else:
    print('False')