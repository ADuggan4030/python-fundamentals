""" Collections Lab - Task 1 """
pizza_faves = ['veggie', 'triple cheese', 'hawaiian',
               'thin crust', 'thick crusty']


def pizza_for():
    for pizza in pizza_faves:
        print(pizza)


# pizza_for()


def pizza_append():
    pizza_faves.append('supreme')
    pizza_faves.append('meat lovers')
    # we can also use insert if we only wanted to write one append line---but
    # have to choose placement of item in list--
    # pizza_faves.insert(4,'meat lovers')
    for pizza in pizza_faves:
        print(pizza)


# pizza_append()


""" Collections Lab -- Task 2 """
amina_fave_movies = {'Theology': {1976: 'The Message',
                                  1980: 'The Lion of the Desert'},
                     'Journeys': {2016: 'The Lost City of Z', 2001: 'A Beautiful Mind',
                                  2007: 'Into the Wild'}}


def my_nested_dictionary():
    for outer_key, value in amina_fave_movies.items():
        print(f'Movie type: {outer_key}')
        for inner_key in value:
            print(f'{inner_key}: {value[inner_key]}')


my_nested_dictionary()
