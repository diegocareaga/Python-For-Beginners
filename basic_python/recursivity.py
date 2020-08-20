def factorial(n):
    """
    Return the factorial of n.
    If n > 0
    """

    if n == 1:
        print('Entre a 1')
        return 1
    print(n)
    
    return n * factorial(n - 1)

n = int(input('Type a integer number: '))
print(factorial(n))