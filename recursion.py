# Recursion: 
# Solve a problem using a simpler version of it

def factorial(number):
    result = 0
    
    if number > 1:
        result = number * factorial(number - 1)
    
    if number == 1:
        result = 1;
        
    return result

print(factorial(4))

def fibonacci(number):
    result = 0
    
    if number > 1:
        result = fibonacci(number - 1) + fibonacci(number -2)
    
    if number <= 1:
        result = 1
    
    return result

print(fibonacci(6))