# This code about Dictionaries and Tuple.

# Hold information about the Basketball Star
# The information we will hold is the
#     1. Number of Championships Won
#     2. How many seasons they played professional Basketball Information = (int,int,int)


# Now lets create variables for each NBA Superstars
billRussell = (11,13)   # Keys and Tuple
samJones = (10,12)
robertHorry = (7,16)
michaelJordan = (6,15)
shaquilleONeil = (4,19)
mikeShah = (0,0)

                       # Now lets create an empty dictionary
nbaDictionary = {}
                       # Now lets populate the dictionary with our entries
                       # The key: The players name
                       # The Value; The players information
nbaDictionary['billRussell'] = billRussell
nbaDictionary['Michael Jordan'] = michaelJordan
nbaDictionary['Sam Jones'] = samJones
nbaDictionary['Robert Horry'] = robertHorry
nbaDictionary['Shaquille o Neil'] = shaquilleONeil
nbaDictionary['Mike Shah'] = mikeShah
            # Finally, lets print out the dictionary to see that our
            # entries have been added
print "==== NBA Superstar Dictionary ===="
print nbaDictionary
print
                       # Now lets query for nba stars in our dictionary who have won
                       # more than 1 championship
for x in nbaDictionary:
             # Now this is a little tricky.
             # Remember, x is our key, so it will retrun something
             # like 'Michael Jordan'
             # We then need to access that key, which is stored in
             # nbaDictionary, and then access the [0] the value, which
             # is our tuple, which represents championships.
    if nbaDictionary[x] [0] > 1:
        print x+' has won '+str(nbaDictionary[x][0]) +' championships!'
print
                       # Print out the players who have a greater than 50% championship record
for x in nbaDictionary:
                       # Access the tuple at championships / seasons played
    if nbaDictionary[x][1] != 0 and float(nbaDictionary[x][0]) / float(nbaDictionary[x][1]) > 0.5:
        print x+' has a good winning percentage'
