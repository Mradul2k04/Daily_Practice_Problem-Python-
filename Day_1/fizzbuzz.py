#The FizzBuzz Classic (Beginner)
#The Goal: Test basic loops and conditional logic.
#The Problem: Print numbers from 1 to 50. For multiples of 3, 
#print "Fizz" instead of the number. For multiples of 5, print "Buzz".
#For numbers which are multiples of both 3 and 5, print "FizzBuzz".


a=int(input("Enter the number 1 to 50 : "))
for i in range(1,a+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)