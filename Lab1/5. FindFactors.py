def find_factors(number):
    factors = []
    # Loop from 1 to the number (inclusive)
    for i in range(1, number + 1):
        # Check if i is a factor of number
        if number % i == 0:
            factors.append(i)
    return factors

# Input from user
number = int(input("Enter a number: "))

# Call the function and display the result
factors = find_factors(number)
print("Factors of", number, "are:", factors)
