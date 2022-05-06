import random

# # list of destinations - 'destinations'
destinations = ['las vegas', 'henderson', 'prim']

# # An option from the list 'destinations' is selected
# # by random.choice()
print(random.choice(destinations))


# # # list of restaurants - 'restaurants' 
restaurants = ['five guys', 'red robins', 'china tango']

# An option from the list 'restaurants' is selected
# by random.choice()
print(random.choice(restaurants))

#list of transportations - 'transportations'
transportations = ['car', 'bus', 'uber']

# An option from the list 'transportations' is selected
# by random.choice()
print(random.choice(transportations))


# # # list of entertainments - 'entertainments'
entertainments = ['movie', 'cirus cirus', 'rave']

# # # An option form the list 'entertainments' is selected
# by random.choice()
print(random.choice(entertainments))

# # # Next step - print the total trip to your user

random_destinations = random.choice(destinations)
print(random_destinations)

random_restaurants = random.choice(restaurants)
print(random_restaurants)

random_transportations = random.choice(transportations)
print(random_transportations)

random_entertainments = random.choice(entertainments)
print(random_entertainments)

# ask your user if they are satisfied with the trip

def my_function(satisfied_with_trip):
    return True 

if my_function('satisfied_with_trip'):
    print("YES!")
else:
    print("NO!")

# IF they are not, re-select the trip features, and display

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

is_the_transportation_adequate = True
while is_the_transportation_adequate is True:
    randomly_re_select = input('yes or no')

    if randomly_re_select == 'yes':
        print('tranit is great')
        is_the_transportation_adequate = False
    elif randomly_re_select == 'no':
        print('tranit is great')
        random_transportation = random.choice(transportations)

is_the_entertainment_tremendous = True
while is_the_entertainment_tremendous is True:
    randomly_re_select = input('yes or no')

    if randomly_re_select == 'yes':
        print('the show is great')
        is_the_entertainment_tremendous = False
    elif randomly_re_select == 'no':
        print('tranit is great')
        random_entertainment = random.choice(entertainments)


# Confirm the completed trip:
# 1. Print all of their choices
#     Can use random_transportations, random_restaurants, random_entertainments, random_locations variables
#     We can print them to the console to display completed trip
# 2. Get user input - did they like the trip?
# 3. If they do like the trip, we can print "Day trip complete, thank you!"
# 4. Elif they don't like the trip, we can print "Day trip incompatable!"


print(random_transportations , random_entertainments , random_destinations , random_entertainments)

select_an_option = input('complete or incomplete')

if select_an_option == 'complete':
    print('trip complete')
    
elif select_an_option == 'incomplete':
    print('imcomplete')
   

