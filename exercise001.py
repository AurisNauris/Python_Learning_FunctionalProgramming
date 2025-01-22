"""
Problem 1: Avoiding Mutable State
Problem: Reverse a String Using Recursion
Write a recursive function to reverse a string without using any mutable variables like a list.
"""
# Option 1
def reverse_string_1(s, acc = ""):
    if len(s) < 1:
        return(acc)
    acc = s[0] + acc 
    return reverse_string_1(s[1:], acc)

print(reverse_string_1("This is a reverse string 111 function."))

# Option 2
def reverse_string_2(s):
    if len(s) < 1:
        return ""
    return reverse_string_2(s[1:])+s[0]
    
print(reverse_string_2("This is a reverse string 222 function."))