# your code goes here
def get_restaurant_ratings(filename):
    """Provides ratings for restaurants.
    """

    the_file = open(filename)

    restaurant_ratings = {}
  
    for line in the_file:  #Open the file and clean up the data.
        line = line.rstrip()
        restaurant = line.split(":")

        #identify the key = restaurant name, and value = rating
        restaurant_name = restaurant[0] 
        restaurant_rating = restaurant[1]

        #pair key with value
        restaurant_ratings[restaurant_name] = restaurant_rating 

    #unpack and sorted dictionary and print key-value pair.
    for restaurant, rating in sorted(restaurant_ratings.items()):
        print "%s is rated at %s." %(restaurant, rating)
       

    the_file.close()


get_restaurant_ratings("scores.txt")