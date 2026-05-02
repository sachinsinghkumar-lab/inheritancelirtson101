class person(object):


        #__init__ is klnown as the contrustuctor to deifn ethe lritson
        def __init__(self, name, idnumber):
                self.name = name
                self.idnumber = idnumber

        def display(self):
                print(self.name)
                print(self.idnumber)

#child class
class Employee(person):
        def __init__(self, name, idnumber, salary, post):
                self.salary=salary
                self.post = post

                person.__init__(self, name, idnumber)

        def displayMSG(self):
                super().display()
                print(f"NAME : {self.name} ID: {self.idnumber} SALARY : {self.salary} POST : {self.post}")

a = Employee('rahul', 886012, 200000, "Intern")

a.displayMSG()
        