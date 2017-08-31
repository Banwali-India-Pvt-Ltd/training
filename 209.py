#lst is the list to sum
#Returns the sum of all the elements
def sum(lst):
      result = 0;
      for item in lst:
          result += item
      return  result
def clear (lst):
    for i in range(len(lst)):
        lst[i] = 0
def random_list(n):
    import  random
    result = []
    for i in range (n):
        rand = random . randrange (100)
        result +=[rand]
    return result
def main():#zero out all the elements of list
    a = [2, 4, 6, 8]
    print (a)#compute and displa
    print (sum(a))
    clear (a)
    print(a) #compute and contents of the list
    print (sum(a))
    a = []    #test empty list
    print (a)
    print (sum(a))
    a = random_list(10)
    print (a)   #test empty list with 10 elements
    print (sum(a))

main()
