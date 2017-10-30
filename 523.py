dict1 = {}                     # Create an empty dictionary
dict2 = dict()                 # Create an empty dictionary 2
dict2 = {"r": 34, "i": 56}     # Initialize to non-empty value
dict3 = dict([("r", 34), ("i", 56)])      # Init from a list of tuples
dict4 = dict(r=34, i=56)       # Initialize to non-empty value 3
dict1["temperature"] = 32      # Assign value to a key
if "temperature" in dict1:     # Membership test of a key AKA key exists
  del dict1["temperature"]     # Delete AKA remove
equalbyvalue = dict2 == dict3
itemcount2 = len(dict2)        # Length AKA size AKA item count
isempty2 = len(dict2) == 0     # Emptiness test
for key in dict2:              # Iterate via keys
  print key, dict2[key]        # Print key and the associated value
  dict2[key] += 10             # Modify-access to the key-value pair
for key in sorted(dict2):      # Iterate via keys in sorted order of the keys
  print key, dict2[key]        # Print key and the associated value
for value in dict2.values():   # Iterate via values
  print value
dict5 = {} # {x: dict2[x] + 1 for x in dict2 } # Dictionary comprehension in Python 2.7 or later
dict6 = dict2.copy()             # A shallow copy
dict6.update({"i": 60, "j": 30}) # Add or overwrite; a bit like list's extend
dict7 = dict2.copy()
dict7.clear()                  # Clear AKA empty AKA erase
sixty = dict6.pop("i")         # Remove key i, returning its value
print dict1, dict2, dict3, dict4, dict5, dict6, dict7, equalbyvalue, itemcount2, sixty