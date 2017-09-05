collection = [24.2, 4, 'word', eval, 19, -0.03, 'end']
for item in collection:
    print(item)         # Print each element



print(len([2, 4, 6, 8]))
a = [10, 20, 30]
print(len(a))



nums = [2, 4, 6, 8]
# Print last element to first (zero index) element
for i in range(len(nums) -1, -1, -1):
    print(nums[i])