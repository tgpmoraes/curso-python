
# Python OOP
import datetime


class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Altera a funcionalidade do método para receber
    # a classe como primeiro argumento ao invés da instância
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        cls(first, last, pay)
        return cls(first, last, pay)

    # Não opera nem na classe e nem na instância
    # especificamente
    @staticmethod
    def is_workday(day):
        return False if day.weekday == 5 or day.weekday == 6 \
            else True


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, *args, prog_lang=None):
        # Classe Employee vai lidar com as variáveis comuns
        # entre as classes (Herança)
        if len(args) > 1:
            super().__init__(*args)

        self.prog_lang = prog_lang

    def from_string(self, *args):
        prog_lang = self.prog_lang
        dev = super().from_string(args[0])
        dev.prog_lang = prog_lang
        return dev


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1 = Developer('Tiago', 'Moraes', 50000, prog_lang='Python')
# emp_2 = Developer('Test', 'Employee', 60000, prog_lang='Java')

# Altera para todas as instâncias
# Employee.set_raise_amt(1.05)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')

# new_emp_1 = Employee(first, last, pay)
# new_emp_1 = Employee.from_string(emp_str_1)
# new_emp_1 = Developer(prog_lang='Ruby')
# new_emp_1 = new_emp_1.from_string(emp_str_1)

# print(emp_1.email)
# print(new_emp_1.fullname())

my_date = datetime.date(2021, 9, 3)

# print(new_emp_1.is_workday(my_date))

# print(emp_1.email)
# print(emp_1.prog_lang)

# print(help(Developer))

# print(emp_2.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

mgr_1 = Manager('Sue', 'Smith', 90000, [emp_1])

# print(mgr_1.email)

# mgr_1.add_emp(emp_2)
# mgr_1.remove_emp(emp_1)
# mgr_1.print_emps()

print(Employee.raise_amt)
print(emp_1.raise_amt)
