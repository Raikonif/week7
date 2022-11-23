from abc import abstractmethod, ABC


class A:
    def __init__(self):
        print('class A')
        self.attribute1 = 'A'  # this is a public attribute
        self._protected_attribute = 'protected attribute'  # this is a protected attribute


class __B:
    pass


class B(A):
    def __init__(self):
        super().__init__()
        print('class B')
        print(self.attribute1)
        self.attribute1 = 100
        print(self.attribute1)
        print(self._protected_attribute)


class Employee(ABC):
    def __init__(self, idd, name):
        self.name = name
        self.id = idd

    @abstractmethod
    def calculate_payroll(self):
        pass

    def __str__(self):
        return f"""Name: {self.name}\nID: {self.id}\n"""


class Administrative(Employee):
    def __init__(self, idd, name, weekly_salary):
        super().__init__(idd, name)
        self.weekly_salary = weekly_salary
        self.employee_type = 'Administrative'

    def calculate_payroll(self):
        return self.weekly_salary


class Manufacturing(Administrative):
    def __init__(self, idd, name, hourly_rate, worked_hours):
        super().__init__(idd, name, hourly_rate * worked_hours)
        self.hourly_rate = hourly_rate
        self.worked_hours = worked_hours
        self.employee_type = 'Manufacturing'

    def calculate_payroll(self):
        return self.hourly_rate * self.worked_hours


class Sales(Administrative):
    def __init__(self, idd, name, weekly_salary, commission):
        super().__init__(idd, name, weekly_salary)
        # self.weekly_salary = weekly_salary
        self.commission = commission
        self.employee_type = 'Sales'

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission


if __name__ == "__main__":
    b = __B()
    isinstance(b, __B)

    bb = B()  # bb is and instance of B
    dir(bb)
    print(dir(bb))

    print(bb._protected_attribute)

    employee = Employee('John Doe')
