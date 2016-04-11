# your code goes here
def get_restaurant_ratings(filename):
    """Provides ratings for restaurants.
    """

    the_file = open(filename)

    restaurant_ratings = {}

    for line in the_file:
        line = line.rstrip()
        restaurant = line.split(":")
        restaurant_name = restaurant[0]
        restaurant_rating = restaurant[1]

    print restaurant
    print restaurant_name
    print restaurant_rating    

    for restaurant_name in restaurant:
        restaurant_ratings[restaurant_name] = restaurant_rating 

    print restaurant_ratings

    the_file.close()


get_restaurant_ratings("scores.txt")