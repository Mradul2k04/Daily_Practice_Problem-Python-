# Practice basic user input, data type conversion, and arithmetic operations.
#Ask the user to input two numbers and a mathematical operator (either +, -, *, or /). 
#Perform the operation and print the final result.


a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
operator =input("Enter the operator (+,-,*,/) : ")
def operators(a,b,operator):
    if operator =="+":
        return(f"Result : {a+b}")
    elif operator=="-":
        return a-b
    elif operator=='*':
        return a*b
    elif operator=='/':
        return a/b if b!=0 else "Error :Division by zero"
    else:
        return "Invalid operator"
        
    
result=operators(a,b,operator)
print(f"Result : {result}")    
    