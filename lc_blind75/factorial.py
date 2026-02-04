def factorial(n):
    fact = 1
    for num in range(1, n+1):
        fact *= num

    return fact

if __name__ == '__main__':
    fact = factorial(5)
    print(f'factorial of 5 is {fact}')
    fact = factorial(6)
    print(f'factorial of 6 is {fact}')
    fact = factorial(1)
    print(f'factorial of 1 is {fact}')
