def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
        return True
def generate_Prime_Series(n):
    prime_series = []
    for num in range(2,n+1):
        if is_prime(num):
            prime_series.append(num)
            return prime_series
n = int(input("ENTER THE UPPER LIMIT (n):"))
Prime_Series = generate_Prime_Series(n)
print(f"Prime number upto{n} are: {Prime_Series}")