""" This is a practice page for my own review """

# set practice
vege_tbls = {'tomato', 'cucumber', 'carrot', 'green beans',
             'lettuce', 'parsley', 'kale'}


def set_practice():
    print(vege_tbls)
    for veggies in vege_tbls:
        print(veggies)


# set_practice()

# This adds an item to your set; set is still unordered and unindexed.
def add_set_practice():
    vege_tbls.add('celery')
    for veggies in vege_tbls:
        print(veggies)


# add_set_practice()

# update() method. This allows you to add multiple items to a set
def update_set_practice():
    vege_tbls.update({'radish', 'onion', 'molokhia', 'cabbage', 'okra'})
    for veggies in vege_tbls:
        print(veggies)


# update_set_practice()


# dictionary collections practice
curRency_bills = {1: 'us dollar - the green back', 2: 'turkish lira - tele',
                  3: 'mexican peso', 4: 'canadian dollar - the loonie',
                  5: ' the euro', 6: 'japanese - yen'}


def get_value_practice():
    value = curRency_bills[3]
    print(value)

    # get_value_practice()

    # def example_arg_practice(*args: int):
    for value in args:
        total = value + 34
        print(f"{value} + 34 = {total}")


# example_arg_practice(5, 10, 15, 20)

# This is 'Try it Yourself' box on page 146 of the book.
# It runs without error; but I do not understand why 6 new lists are printed.
text_mess = ['lol', 'smh', 'brb', 'rofl', 'icymi', 'afaik']


def messages_print():
    for word in text_mess:
        print(word)


messages_print()


def print_mess(text_mess, second_bunch):
    while text_mess:
        current_words = text_mess.pop()
        print(f"Printing model: {current_words}")
        second_bunch.append(current_words)


def show_completed_second_bunch(second_bunch):
    print("\nThe following shortcut words have been printed:")
    for completed_second_bunch in second_bunch:
        print(second_bunch)


text_mess = ['lol', 'smh', 'brb', 'rofl', 'icymi', 'afaik']
second_bunch = []

print_mess(text_mess, second_bunch)
show_completed_second_bunch(second_bunch)
