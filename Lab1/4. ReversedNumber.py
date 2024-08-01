def reverse_number(number):
    # Convert the number to a string
    str_number = str(number)
    
    # Reverse the string using slicing
    reversed_str = str_number[::-1]
    
    # Convert the reversed string back to an integer
    reversed_number = int(reversed_str)
    
    return reversed_number

# Input from user
number = int(input("Enter a number: "))

# Call the function and display the result
print("Reversed number:", reverse_number(number))
