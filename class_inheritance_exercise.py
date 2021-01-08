class Employee:
    """
    Legend of the class: Our company decide to find an easy way to take information about employees and to
    calculate annual bonuses of each one.
    """

    def __init__(self, name, position, company_level):
        self.name: str = name
        self.position: str = position
        self.company_level: str = company_level

    def get_name(self) -> str:  # getter на name
        return self.name

    def employee_info(self) -> str:
        return f"My name is {self.name}, my position in the company is {self.position} and I am level: {self.company_level}"


class EmployeeSalary(Employee):
    def __init__(self, name, position, company_level, monthly_salary):
        super().__init__(name, position, company_level)
        self.monthly_salary: int = monthly_salary

    def calculate_salary(self) -> int:
        return self.monthly_salary


class AnnualBonus(EmployeeSalary):
    def __init__(self, name, position, company_level, monthly_salary, vacations_days_left):
        super().__init__(name, position, company_level, monthly_salary)
        self.vacations_days_left: int = vacations_days_left

    def calculate_annual_bonus(self) -> str:
        bonus = (self.monthly_salary * self.vacations_days_left) * 0.1
        return f"{self.name} your annual bonus is: {bonus} EUR Good job !"


first_employee = AnnualBonus("John", "manager", 4, 3000, 16)
assert first_employee.calculate_annual_bonus() == "John your annual bonus is: 4800.0 EUR Good job !"
# assert that the text when we call the method calculate_annual_bonus will be the same from the assertion
print(first_employee.calculate_annual_bonus())
assert first_employee.get_name() == "John"
# we assert here that the name when we call the method get_name it will be John
print(first_employee.get_name())

employee_of_the_year = AnnualBonus("Samuil", "CTO", 6, 5500, 18)
assert employee_of_the_year.monthly_salary == 5500
# assert that the monthly salary is 5500
print(employee_of_the_year.calculate_annual_bonus())
