import random

destinations = ['las vegas', 'henderson', 'prim']

print(random.choice(destinations))

restaurants = ['five guys', 'red robins', 'china tango']

print(random.choice(restaurants))

transportations = ['car', 'bus', 'uber']

print(random.choice(transportations))


entertainments = ['movie', 'cirus cirus', 'rave']

print(random.choice(entertainments))

random_destinations = random.choice(destinations)
print(random_destinations)

random_restaurants = random.choice(restaurants)
print(random_restaurants)

random_transportations = random.choice(transportations)
print(random_transportations)

random_entertainments = random.choice(entertainments)
print(random_entertainments)

def my_function(satisfied_with_trip):
    return True 

if my_function('satisfied_with_trip'):
    print("YES!")
else:
    print("NO!")


def comfirm_destination():
    is_the_destination_good = True 
    while is_the_destination_good is True:
        randomly_re_select = input('yes or no')

        if randomly_re_select == 'yes':
            print('we would like to stay')
            is_the_destination_good = False
        elif randomly_re_select == 'no':
            print('re-select location')
            random_destinations = random.choice(destinations)
            print(random_destinations)
comfirm_destination()

def comfirm_restaurant():
    is_the_restaurant_satisfying = True
    while is_the_restaurant_satisfying is True:
        randomly_re_select = input('yes or no')

        if randomly_re_select == 'yes':
            print('we_are_satisfied')
            is_the_restaurant_satisfying = False
        elif randomly_re_select == 'no':
            print('we_are_satisfied')
            random_restaurants = random.choice(restaurants)
            print(random_restaurants)
comfirm_restaurant()

def comfirm_transportation():
    is_the_transportation_adequate = True
    while is_the_transportation_adequate is True:
        randomly_re_select = input('yes or no')

        if randomly_re_select == 'yes':
            print('tranit is great')
            is_the_transportation_adequate = False
        elif randomly_re_select == 'no':
            print('tranit is great')
            random_transportation = random.choice(transportations)
comfirm_transportation()

def comfirm_entertainment():
    is_the_entertainment_tremendous = True
    while is_the_entertainment_tremendous is True:
        randomly_re_select = input('yes or no')

        if randomly_re_select == 'yes':
            print('the show is great')
            is_the_entertainment_tremendous = False
        elif randomly_re_select == 'no':
            print('tranit is great')
            random_entertainment = random.choice(entertainments)
comfirm_entertainment()

def my_function(randomly_re_select):
    return True 

if my_function('randomly_re_select'):
    print("selcection_complete!")
else:
    print("selection_incomplete!")

def day_trip_completetion():
    print(random_transportations , random_restaurants , random_destinations , random_entertainments)

    select_an_option = input('complete or incomplete')

    if select_an_option == 'complete':
        print('trip complete')
        
    elif select_an_option == 'incomplete':
        print('incomplete')
day_trip_completetion()