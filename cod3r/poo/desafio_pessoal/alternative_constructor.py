class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@email.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    # alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        cls(first, last, pay)
        return cls(first, last, pay)


class Developer(Employee):

    def __init__(self, first, last, pay, prog_lang=None):
        super().__init__(first, last, pay)

        self.prog_lang = prog_lang


emp_1 = Developer('Tiago', 'Moraes', 50000, 'Python')

emp_str_1 = 'John-Doe-70000'

new_emp_1 = Employee.from_string(emp_str_1)

print(emp_1.fullname())
print(new_emp_1.fullname())
