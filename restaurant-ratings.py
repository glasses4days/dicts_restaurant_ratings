# your code goes here
def get_restaurant_ratings(filename):
    """Provides ratings for restaurants.
    """

    the_file = open(filename)

    restaurant_ratings = {}
    alphabetical_restaurant_lst = []

    for line in the_file:  #Open the file and clean up the data.
        line = line.rstrip()
        restaurant = line.split(":")

        #identify the key = restaurant name, and value = rating
        restaurant_name = restaurant[0] 
        restaurant_rating = restaurant[1]

        #pair key with value
        restaurant_ratings[restaurant_name] = restaurant_rating 

    # unpack dictionary and sort key- value pair into a list.
    for restaurant, rating in restaurant_ratings.items():
        alphabetical_restaurant = "%s is rated at %s." %(restaurant, rating)
        alphabetical_restaurant_lst.append(alphabetical_restaurant)
        alphabetical_restaurant_lst.sort()
    
    #print restaurant with value in alphabetical order.
    for index in alphabetical_restaurant_lst:
        print index 




    the_file.close()


get_restaurant_ratings("scores.txt")