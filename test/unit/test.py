# unit test pylint log (format test)
class unitTest():
    def __init__(self):
        self.testcase = []
        self.size = 0
        self.logTest()
    
    def logTest(self):
        with open("test/unit/test.log") as test:
            for line in test:
                self.testcase.append(line)
                self.size += 1
    
    def 