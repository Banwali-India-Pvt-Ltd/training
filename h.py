# Plays the guessing game higher or lower
# (originally written by Josh Cogliati, improved by Quique, now improved
# by Sanjith, further improved by VorDd, with continued improvement from
# the various Wikibooks contributors.)

# This should actually be something that is semi random like the
# last digits of the time or something else, but that will have to
# wait till a later chapter.  (Extra Credit, modify it to be random
# after the Modules chapter)

# This is for demonstration purposes only.
# It is not written to handle invalid input like a full program would.

answer = 23
question = 'What number am I thinking of?  '
print ('Let\'s play the guessing game!')

while True:
    guess = int(input(question))

    if guess < answer:
        print ('Little higher')
    elif guess > answer:
        print ('Little lower')
    else:  # guess == answer
        print ('MINDREADER!!!')
    break