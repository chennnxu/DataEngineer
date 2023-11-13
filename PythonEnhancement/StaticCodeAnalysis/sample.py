"""
Static code analysis sample
"""
# pip3 install pylint==2.11.1
# terminal run pylint sample.py


def add(number1, number2):
    """
    Add function get the sum of two numbers
    """
    return number1 + number2


NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
