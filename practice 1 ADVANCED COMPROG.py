class person:
    def __init__(self, frame, lname):
        self.firstname = frame
        self.lastname =lname

    def printname(self):
            print(self.firstname, self.lastname)

#Use the person class to create an object, and then execute

x = person("donny", "pangilinan")
x.printname()           
