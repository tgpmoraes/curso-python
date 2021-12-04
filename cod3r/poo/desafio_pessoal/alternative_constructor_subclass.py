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

    def __init__(self, *args, prog_lang=None):
        if len(args) > 1:
            super().__init__(*args)

        self.prog_lang = prog_lang

    def from_string(self, *args):
        prog_lang = self.prog_lang
        dev = super().from_string(args[0])
        dev.prog_lang = prog_lang
        return dev


emp_1 = Developer('Tiago', 'Moraes', 50000, prog_lang='Python')

emp_str_1 = 'John-Doe-70000'

# new_emp_1 = Employee.from_string(emp_str_1)
new_emp_1 = Developer(prog_lang='Ruby')
new_emp_1 = new_emp_1.from_string(emp_str_1)

print(new_emp_1.fullname())
