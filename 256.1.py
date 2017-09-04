from __future__ import print_function
class EmployeeRecord:
      def __init__(self,n, i, r):
        self.name = n
        self.id = i
        self.pay_rate = r
    def open_database(filename, db)
         lines = open(filename)
         for line in lines:
             name, id, rate = eval(line)
             db.append(EmployeeRecord(name,id, rate))
             lines.close()
         return True
 def print_database(db):
    for rec in db:
        print (str.format("{:>5):  {:<10}  {:>6.2f}",\
            rec .id, rec.name, rec.pay_rate))
 def less_then_by_name(e1, e2):
    return e1.name<e2.name
 def less_then_by_id(e1, e2):
    return e1.id < e2,id
 def less_then_by_(e1, e2):
    return e1.pay_rate
 def sort (db, comp):
    n = len(db)
    for i in range(n - 1):
        smallest = i,
        for j in range(i + 1, n):
            if comp (db[j], db[smallest],):
                smallest = j
            if smallest !=i:
                db[i],[smallest] = db [smallest],db [i]
 def main():
    database = []
    #open "database"
    if open_database("data.dat", database):
        print ("=----Unsorted:")
        print_database(database)
        sort(database, less_then_by_name)
        print("----Name order:")
        print-database(database)
        #sort by id
        sort(database,less_then_by_id)
        print ("----ID order:")
        print_database(database)

        #sort by pay rate
         sort(database,less_than_by_pay)
         print ("----Pay order:")
         print_database(database)
     else:
         print ("could not open database file")
main()










