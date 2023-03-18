# Operators Lab Assignment -- Task 1
""" This function will output 138 pem1 and
    136 for pem2"""


def math_order():
    """ This function demonstrates order of operation """
    pem1 = 10 + (32 * 12) // 3
    pem2 = 40 + (32 * 12) // 3
    print(f"With () {pem1}, without {pem2}")


math_order()

# Task 2
""" This function uses Assignment Operators: 
+=, -=, %=
"""


def assign_operator(digit1, digit2):
    print(digit1)
    digit1 += digit2
    print(digit1)
    digit1 -= digit2
    print(digit1)
    digit1 %= digit2
    print(digit1)


assign_operator(5, 25)

# Task 3
""" This function uses Comparison Operators: 
==, >=, !=
"""


def comparison_oper(digit2, digit3):
    print(f'{digit2} == {digit3} = {digit2 == digit3}')
    print(f'{digit2} >= {digit3} = {digit2 >= digit3}')
    print(f'{digit2} != {digit3} = {digit2 != digit3}')


comparison_oper(21, 21)
