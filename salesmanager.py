from employee import Employee
class SalesManager(Employee):
    def __init__(self, name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails, salesTarget):
        """Initialize a SalesManager object, inheriting from Employee"""
        super().__init__(name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails)
        self.salesTarget = salesTarget

    # Getter and setter for salesTarget
    def get_salesTarget(self):
        return self.salesTarget

    def set_salesTarget(self, salesTarget = " "):
        self.salesTarget = salesTarget

    def __str__(self):
        return f"{super().__str__()}\nSales Target: {self.salesTarget}"
