class Tester:
    def __init__(self):
        self.__error_count = total_count = 0
        print ("---------------------------------")
        print (" |       Testing           ")
        print ("+---- ---- ------- --------- ----")
    def check_equals(self,msg,expected, actual):
        print (",[",msg,"] ")
        self.__total_count +=1
        if expected == actual:
            print ("ok")
        else:
            self.__error_count += 1
            print ("*** Failed! Expected:", expected, " actual:",actual)
    def report_results(self):
        print ("+-------------------------------------")
        print ("|", self.__total_count,"tests run")
        print ("|", self.__total_count - self.error_count, "passed")
        print ("|", self.__total_count, "failed")
        print ("+-----------------------------------------")