# my first Python Lab Assignment
# All About Strings-- Tasks 1 - 3

# Task 1
delta: str = ' This statement has empty spaces '


def get_pos_value():
    print(delta[6:17])


def get_neg_value():
    print(delta[-17:-6])


get_pos_value()
get_neg_value()

# Task 2
method_lab_assign: str = ' This statement has empty spaces '
print(method_lab_assign.strip)
print(method_lab_assign.upper)
print(method_lab_assign.find('eme'))
print(method_lab_assign.count('s'))



# def get_strip_value():
   # print(method_lab_assign.strip())


# def get_upper_value():
   # print(method_lab_assign.upper())


# def get_find_value():
    # print(method_lab_assign.find('eme'))


# def get_count_value():
    # print(method_lab_assign.count('s'))

#  jfdlfjdkf
# get_strip_value()
# get_upper_value()
# get_find_value()
# get_count_value()


# Task 3 - Jack & Jill Poem
# Retrieved from: https://allnurseryrhymes.com/jack-and-jill/
# This poem will be formatted from one string variable line with escape as follows:
# Jack and Jill went up the hill
# To fetch a pail of water
# Jack fell down and broke his crown
# And Jill came tumbling after
value_a = " Jack and Jill went up the hill \n To fetch a pail of water " \
          "\n Jack fell down and broke his crown \n And Jill came tumbling after. "
print(value_a)
