from model import Department,Task,Employee,User
from enums import Priority,UserRole
from generator import UniqueIdGenerator
from database_controller import EmployeeDatabaseManager
import random

class UserDataProvider:
    def __init__(self):
        self.__user_list=[]
        self._create_user_list()
        
        
    def _create_user_list(self):
        user1 = User("1","1",UserRole.ADMIN)
        user2 = User("2","2",UserRole.EMPLOYEE)
        user3 = User("3","3",UserRole.EMPLOYEE)
        user4 = User("4","4",UserRole.INTERN)
        self.__user_list.append(user1)
        self.__user_list.append(user2)
        self.__user_list.append(user3)
        self.__user_list.append(user4)

    @property
    def user_list(self):
        return self.__user_list
    
class DataProvider:
    def __init__ (self):
        self.__departments = []
        self._create_department_list()
    
    
    def _create_department_list(self):
        unique_id = random.randint(1,1000)
        department1_name = "Sales"
        department1_emplyoee_list = self._create_department_employees(department1_name)
        department1 = Department(unique_id,department1_name, department1_emplyoee_list)    
    
        unique_id = random.randint(1,1000)
        department2_name = "Management"
        department2_emplyoee_list = self._create_department_employees(department2_name)
        department2 = Department(unique_id, department2_name,department2_emplyoee_list)    
    
        unique_id = random.randint(1,1000)
        department3_name = "Development"
        department3_emplyoee_list = self._create_department_employees(department3_name)
        department3 = Department(unique_id,department3_name, department3_emplyoee_list)    
    
        self.__departments.append(department1)
        self.__departments.append(department2)
        self.__departments.append(department3)
        
        
    def _create_department_employees(self,department_name):
        employee_list = []
        for index in range (1,4):
            unique_id = UniqueIdGenerator.generate_id()
            employee_list.append(Employee(unique_id,f"{department_name} Man{index}",f"{department_name} Street{index}",f"{department_name}.man{index}@{department_name}.com",f"+3897789{index}",self.create_employee_tasks(department_name,index)))
        
        return employee_list
    
    def create_employee_tasks(self,department_name,employee_index):
        task_list = []
        for index in range(1,5):
            priority = Priority.HIGH if index % 2 == 0 else Priority.LOW
            #TODO
            task_list.append(Task(f"{department_name}Task{index+employee_index}",f"{department_name} task description {index+employee_index} ",priority))
        
        return task_list
    
    
    
    @property
    def department_list(self):
        return self.__departments