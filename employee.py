class Employee:
    ''' Class represent Employee'''
    def __init__(self, name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails):
        """Initialize an Employee object with attributes"""
        self._name = name
        self._employeeID = employeeID
        self._department = department
        self._jobTitle = jobTitle
        self._basicSalary = basicSalary
        self._age = age
        self._dateOfBirth = dateOfBirth
        self._passportDetails = passportDetails

    # Getter and setter methods for each attribute

    def get_name(self):
        return self._name

    def set_name(self, name = " "):
        self._name = name

    def get_employeeID(self):
        return self._employeeID

    def set_employeeID(self, employeeID = " "):
        self._employeeID = employeeID

    def get_department(self):
        return self._department

    def set_department(self, department = " "):
        self._department = department

    def get_jobTitle(self):
        return self._jobTitle

    def set_jobTitle(self, jobTitle = " "):
        self._jobTitle = jobTitle

    def get_basicSalary(self):
        return self._basicSalary

    def set_basicSalary(self, basicSalary = " "):
        self._basicSalary = basicSalary

    def get_age(self):
        return self._age

    def set_age(self, age = 0):
        self._age = age

    def get_dateOfBirth(self):
        return self._dateOfBirth

    def set_dateOfBirth(self, dateOfBirth = " "):
        self._dateOfBirth = dateOfBirth

    def get_passportDetails(self):
        return self._passportDetails

    def set_passportDetails(self, passportDetails = " "):
        self._passportDetails = passportDetails

    def __str__(self):
        return f"Name: {self._name}\nEmployee ID: {self._employeeID}\nDepartment: {self._department}\nJob Title: {self._jobTitle}\nBasic Salary: {self._basicSalary}\nAge: {self._age}\nDate of Birth: {self._dateOfBirth}\nPassport Details: {self._passportDetails}"
