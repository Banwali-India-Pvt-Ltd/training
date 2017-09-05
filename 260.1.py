# Chapter 12

class Tester:
    def __init__(self):
        self.__error_count = self.__total_count = 0
        print("+---------------------------------------")
        print("|    Testing                       ")
        print("+---------------------------------------")

    def check_equals(self, msg, expected, actual):
        print("[", msg, "] ")
        self.__total_count += 1         # Count this test
        if expected == actual:
            print("OK")
        else:
            self.__error_count += 1     # Count this failed test
            print("*** Failed! Expected.", expected, " actual:", actual)
    def report_results(self):
        print("+---------------------------------------")
        print("|", self.__total_count, "tests run")
