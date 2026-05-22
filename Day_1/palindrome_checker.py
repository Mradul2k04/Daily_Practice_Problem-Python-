# Palindrome Checker (Intermediate)
#The Goal: Test string manipulation and pointer logic.
#The Problem: Write a function that checks if a given 
#string reads the same backward as forward (e.g., "radar" or "racecar").
# Ignore spaces, capitalization, and punctuation.

text=input("Enter the word from user : ")

def palindrome(text):
    check_test=""
    for i in text.lower():
        if i.isalnum():
            check_test +=i
    return check_test==check_test[::-1]
if palindrome(text):
    print("yes .it is palindrome")
else:
    print("No,it is not a palindrome")
            

            
        