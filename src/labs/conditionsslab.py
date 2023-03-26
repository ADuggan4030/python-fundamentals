def easy_if(num1, num2):
    if num1 == num2:
        print('num1 is equal to num2')
    else:
        print('num1 is not equal to num2')


# easy_if(23, 77)


word1: str = 'Python is interesting'
word2: str = 'Python is mind trippy'


def simple_if():
    if word1 == word2:
        print('Python is amazing and these values are equal.')
    else:
        print(
            "Python is still amazing but \n these \n   values \n        are \n          not \n             equal.  :) ")


# simple_if()


def student_marks(alphae):
    if alphae == "E" :
        print("Excellent")
    elif alphae == "V" :
        print("Very Good")
    elif alphae == "G" :
        print("Good Job")
    elif alphae == "A" :
        print("Average")
    elif alphae == "F" :
        print("Failed")
    else:
        print("Not a Valid Grade")


student_marks("A")
