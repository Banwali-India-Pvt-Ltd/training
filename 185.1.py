# Chapter 9
# Page No. 185.1

# The elements of a list extracted with [] can be treated as any other variable; for example,
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(nums[3])       # Print the fourth element
print(nums[0] + nums[9])/2;     # The third element is the average of two other elements
nums[1], nums[4] = eval(input("Enter a, b: "))     # Assign elements at indices 1 and 4 from user input
                                                   # using tuple assignment
