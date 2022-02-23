# Import datetime from datetime
from datetime import datetime


class Employee:

    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")

        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self, raise_amount):
        self.salary = self.salary + raise_amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12

    # Add the __str__() method
    def __str__(self):
        return """
Employee name: {}
Employee salary: {}""".format(self.name, self.salary)


emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)
emp2 = Employee("Lara da Silva", 50000)
print(emp2.salary)
emp2.give_raise(1500)
print(emp2.salary)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp2.monthly_salary()

# Print mon_sal
print(mon_sal)

emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)
