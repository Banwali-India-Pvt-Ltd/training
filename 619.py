def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist