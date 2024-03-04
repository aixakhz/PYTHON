#Debugging

#PART 2.1
for i in range (51):
    print(i)

#PART 2.2
#there's an error with the word "square"
    #because "square" is not recognized
#previous command:
    #"lis=[2,3,4]"
    #"square(lis)"
#new command
ls1=[2,3,4]
ls2=[]
for i in ls1:
    ls2.append(i**2)
print(ls2)
#I used a for loop to fix the issue. I also used the "append" command we learned.

#PART 2.3
listA=(1,2,3,4,5,6,7,8,9,10)
listB=(20,21,22,23,24,25,26,27,28,29,30)
#I did not want to write out the same statement I did for 2.1, so I decided to...
#...write out each integer individually.
listC=(listA+listB)
#This way I was able to combine all the numbers.
for i in listC:
    if i%2!=0:
        print(i)
#I saw it was easiest to create a nest loop for this type of problem.
#We recall that "%" means the variable is divided and returns the value of the remainder
#"!=" means not equal to

#PART 3.1
a=[1,2,'?',4,5]
   #after first typing in "?" I got an "invalid syntax" that specified what line the error was in
    #I had to put the question mark in quotations to fix this issue
b=['?',7,8,'?',10]
c=[11,'?',13,14,'?']
d=[16,17,'?',19,20]
e=['?',22,23,'?',25]
for i in a,b,c,d,e:
    print(i)

#PART 4
x=(1,1,2,3,4,4)
x=set(x)
#previously I was not getting any output even with "print(x)"
print(x)
#I used the "print" debugging statement to see where my issue was