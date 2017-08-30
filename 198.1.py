# Chapter 9
# 9.4 Slicing

lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst)          # Print [10, 20, 30, 40, 50, 60, 70, 80]
print(lst[0:3])     # Print [10, 20, 30]
print(lst[4:8])     # Print [50, 60, 70, 80]
print(lst[2:5])     # Print [30, 40, 50]
print(lst[-5:-3])   # Print [40, 50]
print(lst[:3])      # Print [10, 20, 30]
print(lst[4:])      # Print [50, 60, 70, 80]
print(lst[:])       # Print [10, 20, 30, 40, 50, 60, 70, 80]
print(lst[-100:3])  # Print [10, 20, 30]
print(lst[4:100])   # Print [50, 60, 70, 80]

