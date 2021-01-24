class Person(object):
    def __init__(self, name, idNumber):
        self.name = name
        self.idNumber = idNumber

    def display(self):
        print(self.name)
        print(self.idNumber)

class Employee(Person):
    def __init__(self, name, idNumber, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self,name, idNumber)

    def display2(self):
        print(self.name)
        print(self.idNumber)
        print(self.salary)
        print(self.post)
        

a = Employee("Rahul", 4798274832794, 4893248290, "Intern")
a.display()
print("=====================")
a.display2()