from enum import Enum

class Priority(Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    
    
class UserRole(Enum):
    ADMIN = 1
    EMPLOYEE = 2
    INTERN = 3
    
class UserFeatures(Enum):
    EMPLOYEES = 1
    DEPARTMENTS = 2
    PAYROLLS = 3
    HOLIDAYS = 4
    ACCOUNTS = 5
    CUSTOMERS = 6
    SALES = 7
    CALENDAR = 8
    TASK = 9
    SIGN_OUT = 10