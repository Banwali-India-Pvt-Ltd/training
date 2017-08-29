def changeme(mylist):
    mylist.append({1,2,3,4});
    print("values inside the function: ", mylist)
    return
mylist = [10,20,30];
changeme(mylist);
print("values outside the function: ", mylist)