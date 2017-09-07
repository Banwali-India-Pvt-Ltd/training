# About function

# Illustrate a global constant being used inside function.

PI = 3.1415        # Global constant only place the value of Pi si set

def circleArea(radius):
    return PI*radius*radius    # use value of global constant PI

def circleCircumference(radius):
    return 2*PI*radius     # use value of global constant PI

def main():
    print('Circle are with radius 5: ', circleArea(5))                # Call the circleArea function
    print('Cirlecumference with radius 5: ', circleCircumference(5))  # Call the circleCircumference

main()  # Call the main function