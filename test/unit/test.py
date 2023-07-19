# unit test pylint log (format test)
import matplotlib.pyplot as plt
class FormatTest():
    def __init__(self):
        self.testcase = []
        self.import_error = []
        self.white_space_error = []
        self.variable_error =[]
        self.size = 0
        self.logTest()
    
    def logTest(self):
        with open("test/unit/test.log") as test:
            for line in test:
                self.testcase.append(line)
                self.size += 1
    
    def processingTest(self):
        for item in self.testcase:
            if item.find("import") == True:
                self.import_error.append(item)
            elif item.find("space") == True:
                self.white_space_error.append(item)
            elif item.find("variable") == True:
                self.variable_error.append(item)
    
    def display(self):
        x = ["library", "space and code style", "variable"]
        y = [len(self.import_error), len(self.white_space_error), len(self.variable_error)]
        p = plt.bar(x, y)
        p.plot()

class TimeTest():
    def __init__(self):
        self.logTest()
    
    def logTest():
        run_terminate = "python3 -m memory_profiler src/main.py"
   
        
    