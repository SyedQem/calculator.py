# Calculator.py Version 1.0


def addition(op1: float, op2: float) -> float:
    
    """ 
    Takes 2 numbers and adds them together.
    
    addition(1, 5)
    >>> 6.0
    
    addition(2.0, 5.6)
    >>> 7.6
    
    """
    
    sum = op1 + op2
    sum = float(sum)
    
    return sum

def multiplication(op1: float, op2: float) -> float:
    
    """
    
    Takes 2 numbers and multiplies them by one another.
    
    multiplication(2, 5)
    >>> 10.0
    
    multiplcation(6, 9)
    >>> 54.0
    
    """
    
    product = op1 * op2
    
    product = float(product)
    
    return product


print("-------------------------------------------------------------")



op1 = input("Please input the first number: ")
op2 = input("Please input the second number: ")

op1 = int(op1)
op2 = int(op2)

operation = input("Please input the type of operation that you'd like to conduct: ") # Only supports addition and multiplication.

if operation == "+":
    
    
    print("The sum results to: ")
    print(addition(op1, op2))

elif operation == "*":
    
    print("The product results to: ")
    print(multiplication(op1, op2))
    
print("-------------------------------------------------------------")