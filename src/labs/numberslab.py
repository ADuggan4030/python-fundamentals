# my second Python Lab Assignment
# All About Numbers -- Tasks 1-2
# Task 1

# int with numeric seperator
amount: int = 34_038
# float with numeric seperator
value: float = 45_838.8734
# int with numeric seperator
very_small_num: int = -3_695_365
# int with numeric seperator
Binary: int = 0b_0110_0010_1011
# int with numeric seperator
Hexadecimal: int = 0x_174C0

# Task 2 - Value of 29
# Lab Assign Instructions:
""" Write a function to contain the following. 
With the literal value of 29 as a reference, 
write the literal representation for Hexadecimal, 
Binary and Octal to their own variables. 
Also within the function, write a print function 
for each variable to ensure their output is 29.
Below functions represent Numeric types based
on the number 29. 
"""


def match_num_types(value1: 29):
    """ The below methods will provide
    numeric type based on the argument
    supplied.
    """
    print(bin(value1))
    print(oct(value1))
    print(hex(value1))
    print(value1)


match_num_types(29)


# hexadecimal
def basic_hexadecimal():
    print(0x1d)


# binary
def basic_binary():
    print(0b11101)


# octal
def basic_octal():
    print(0o35)


basic_hexadecimal()
basic_binary()
basic_octal()
