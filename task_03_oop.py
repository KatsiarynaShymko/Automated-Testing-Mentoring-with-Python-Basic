from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar, Union


@dataclass
class Employee(ABC):
    """
    Template of Employee profile

    Attributes:
        name (str): Name of employee
        emp_id (str): Unique identifier for employee. Default None
        company (Company): The company this employee is currently employed by. Default None

    Class Attributes:
        _last_assigned_id: Class-level attribute used to generate unique employee IDs

    Methods:
        calculate_payment(): Abstract method to calculate employee's payment
        leave_company(): Removes the employee from their current company
    """

    name: str
    emp_id: str = field(init=False, default=None)
    _company: "Company" = field(init=False, default=None)

    _last_assigned_id: ClassVar[int] = 0

    def __post_init__(self) -> None:
        """
        Automatically assigns a unique employee ID after the object is initialized
        :return:
            E + emp_id (i.e. E1, E2 ..., En)
        """
        Employee._last_assigned_id += 1
        self.emp_id = f"E{Employee._last_assigned_id}"

    @property
    def company(self) -> ["Company"]:
        """
        The company this employee is currently associated with
        :return:
            Company or None: The company the employee works for, or None if unemployed
        """
        return self._company

    @company.setter
    def company(self, value: ["Company"]) -> None:
        """
        Sets the company the employee is associated with
        :param value:
            Company
        :return:
            Updated company
        """
        self._company = value

    @abstractmethod
    def calculate_payment(self) -> Union[int, float]:
        """
        Will be implemented in the subclasses
        """
        pass

    def leave_company(self) -> bool:
        """
        The method should check if the employee is currently employed by a company

        :return:
            If yes, the method should call the fire method of the company to remove the employee from the company's list of employees
            If not - a message saying that the employee is not currently employed by any company
        """
        if self.company is None:
            return False
        else:
            self.company.fire(self)
            return True


@dataclass
class HourlyEmployee(Employee):
    """
    Employee paid based on an hourly rate

    Inherits from the abstract Employee base class and implements
    payment calculation logic specific to hourly-paid employees

    Attributes:
        hourly_rate (int): hourly rate

    Methods:
        calculate_payment(): Returns weekly payment based on a 40-hour work week
    """

    _hourly_rate: int

    @property
    def hourly_rate(self) -> int:
        """
        Setter of hourly_rate
        :return: Current hourly rate of employee
        """
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, value: int) -> None:
        """
        Updates hourly rate of employee
        :param value: new hourly rate of employee
        :return: assigns new hourly rate
        """
        self._hourly_rate = value

    def calculate_payment(self) -> int:
        """
        Returns weekly payment based on a 40-hour work week
        :return: hourly rate multiplied by 40
        """
        return self._hourly_rate * 40


@dataclass
class SalariedEmployee(Employee):
    """
    Employee paid based on salary

    Inherits from the abstract Employee base class and implements
    payment calculation logic specific to employees with salary

    Attributes:
        salary (int): employee's salary

    Methods:
        calculate_payment(): Returns weekly payment based on a 40-hour work week
    """

    _salary: int

    @property
    def salary(self) -> int:
        """
        Getter of employee's salary
        :return: employee's salary
        """
        return self._salary

    @salary.setter
    def salary(self, value: int) -> None:
        """
        Setter of employee's salary
        :param value: new salary of employee
        :return: assigns new salary for employee
        """
        self._salary = value

    def calculate_payment(self) -> float:
        """
        Returns weekly payment
        :return: Salary divided by 4, so one week payment is calculated
        """
        return self._salary / 4


class Domain(Enum):
    """
    Business domains a company can operate in
    """

    TECHNOLOGY = "TECHNOLOGY"
    HEALTHCARE = "HEALTHCARE"
    RETAIL = "RETAIL"


@dataclass
class Company:
    """
    Represents a company that can hire, fire, and manage employees

    Attributes:
        name (int): Unique identifier or name of the company
        domain (Domain): Business domain of the company
        employees (list): List of currently employed employees

    Methods:
        hire(employee): Hires an employee and assigns them to the company
        fire(employee): Removes an employee from the company
        raise_pay(employee, amount): Increases the employee's pay (salary or hourly rate)
        __repr__(): Returns a string representation of the company.
    """

    name: int
    domain: Domain
    employees: list = field(default_factory=list)

    def hire(self, employee: Employee) -> bool:
        """
        Hires an employee and assigns to the company

        Checks if the employee is already hired by any company or already in the current company's employee list. If not, adds them.

        :param employee: existing employee instance
        :return: A message indicating the result of the hiring attempt (str)
        """
        if employee.company is not None:
            return False
        elif employee in self.employees:
            return False
        else:
            self.employees.append(employee)
            employee.company = self
            return True

    def fire(self, employee: Employee) -> bool:
        """
        Fires an employee from the company

        Removes the employee from the employee list and clears their company association
        :param employee: employee to be fired
        :return: A message indicating the result (str)
        """
        if employee not in self.employees:
            return False
        else:
            self.employees.remove(employee)
            employee.company = None
            return True

    def raise_pay(self, employee: Employee, amount: int) -> str:
        """
        Increases the salary or hourly rate of an employee if employee is hired
        :param employee: employee whose pay should be raised
        :param amount: amount to increase
        :return: message indicating the result (str)
        """
        if employee.company is self:
            if isinstance(employee, HourlyEmployee):
                employee.hourly_rate += amount
                return "Hourly rate is increased"
            elif isinstance(employee, SalariedEmployee):
                employee.salary += amount
                return "Salary is increased"
            else:
                return "Unknown type"
        else:
            return "Employee is not employed by company"

    def __repr__(self) -> str:
        """
        Returns a string representation of the company. Includes the company's name, domain, and number of employees
        :return: formatted string describing the company
        """
        return f"Company({self.name}, {self.domain.name}, Employees: {len(self.employees)})"


if __name__ == "__main__":
    # Create 2 companies with different domains.
    print("Create 2 companies with different domains".center(150, "-"))
    company1 = Company(101, domain=Domain.TECHNOLOGY)
    company2 = Company(202, domain=Domain.HEALTHCARE)
    print(company1)
    print(company2)

    # Create few various types of employees.
    print("Create few various types of employees".center(150, "-"))
    employee1 = HourlyEmployee("Bona Hourly-Sforca", 25)
    employee2 = SalariedEmployee("Kazimir Salary-Kaydashev", 3000)
    employee3 = HourlyEmployee("Jane Hourly-Air", 80)
    employee4 = SalariedEmployee("Mister Salary-Darcy", 1000)
    print(employee1)
    print(employee2)
    print(employee3)
    print(employee4)

    # Hire of various types of employees (hire method).
    print("Hire of various types of employees (hire method)".center(150, "-"))
    print(company1.hire(employee1))
    print(company1.hire(employee2))
    print(company2.hire(employee3))

    # Verify that employees are added to the company's list of employees, emp_id aren’t duplicated.
    print(
        "Verify that employees are added to the company's list of employees, emp_id aren’t duplicated".center(
            150, "-"
        )
    )
    print("\nCompany 101 employees:")
    for emp in company1.employees:
        print(emp)

    print("\nCompany 202 employees:")
    for emp in company2.employees:
        print(emp)

    all_employees = company1.employees + company2.employees
    all_ids = [emp.emp_id for emp in all_employees]
    if len(all_ids) == len(set(all_ids)):
        print("There are no duplicated ids'")
    else:
        print("There are duplicated ids'")

    # Attempting to hire the same employee twice.
    print("Attempting to hire the same employee twice".center(150, "-"))
    print(company2.hire(employee4))
    print(company2.hire(employee4))

    # Remove employees from the company using the fire method. Verify that employees are no longer in the company's list of employees.
    print("Remove employees from the company using the fire method".center(150, "-"))
    print(company1.fire(employee1))
    print(company2.fire(employee4))
    if (employee1 in company1.employees) or (employee4 in company2.employees):
        print("There is an issue with firing employees")
    else:
        print("Employees are no longer in the company's list of employees")

    # Attempting to fire an employee not employed by the company.
    # Verify that attempting to fire an employee not employed by the company doesn't affect the employee list.
    print("Attempting to fire an employee not employed by the company".center(150, "-"))
    print(company1.fire(employee1))
    print("\nCompany 101 employees:")
    for emp in company1.employees:
        print(emp)

    print("\nCompany 202 employees:")
    for emp in company2.employees:
        print(emp)

    # Set and get salaries/hourly_rates for various employees;
    print("Set and get salaries/hourly_rates for various employees".center(150, "-"))
    print(f"Employee hourly rate is {employee1.hourly_rate}")
    employee1.hourly_rate = 80
    print(f"Employee hourly rate was changed to {employee1.hourly_rate}")
    print(f"\nEmployee salary is {employee2.salary}")
    employee2.salary = 555
    print(f"Employee salary was changed to {employee2.salary}")

    # Call the calculate_payment method and verify that the payment is calculated correctly.
    print(
        "Call the calculate_payment method and verify that the payment is calculated correctly".center(
            150, "-"
        )
    )
    print(
        f"{employee1.name}'s hourly rate is {employee1.hourly_rate}, so if we calculate payment it will be {employee1.calculate_payment()}"
    )
    print(
        f"{employee4.name}'s salary is {employee4.salary}, so if we calculate payment it will be {employee4.calculate_payment()}"
    )

    # Increase the salary or hourly_rate of an employee using the raise_pay method.
    print(
        "Increase the salary or hourly_rate of an employee using the raise_pay method".center(
            150, "-"
        )
    )

    print(f"Employee's salary before raising: {employee2.salary}")
    print(company1.raise_pay(employee2, 15))
    print(f"Employee's salary after raising: {employee2.salary}")

    print(f"\nEmployee's hourly rate before raising: {employee3.hourly_rate}")
    print(company2.raise_pay(employee3, 15))
    print(f"Employee's hourly rate after raising: {employee3.hourly_rate}")

    # Attempting to raise_pay for an employee not employed by the company
    print(
        "Attempting to raise_pay for an employee not employed by the company".center(
            150, "-"
        )
    )
    print(company1.raise_pay(employee4, 100))

    # For an employee currently employed by a company, call the leave_company method
    print(
        "For an employee currently employed by a company, call the leave_company method".center(
            150, "-"
        )
    )
    print(employee2.leave_company())
    print(employee2.leave_company())

    # Call the __repr__ method of the Company class and verify that it returns a string representation in the correct format.
    print(
        "Call the __repr__ method of the Company class and verify that it returns a string representation in the correct format".center(
            150, "-"
        )
    )
    print(repr(company1))
    print(repr(company2))