class Job:
    instances = dict()
    rate = 1.04

    def __init__(self, location, salary, description, fee)  :
        self.location = location
        self.salary  = salary
        self.description  = description
        self.fee  = fee
        self.instances[self.location] = location
        self.instances[self.fee] = fee

    def Charge(self):
        self.fee = int( self.fee + Job.rate)



Job1 = Job("london",23000,"Accounts Assistant",1200)
Job2 = Job("london",25000,"Accounts Assistant",500)

print(Job.instances)