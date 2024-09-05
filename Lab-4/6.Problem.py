def check_string(input_string):

    if input_string == "yes" or input_string == "YES" or input_string == "Yes":
        print("Yes")
    else:
        print("No")


input_string = input("Enter a string: ")


check_string(input_string)
