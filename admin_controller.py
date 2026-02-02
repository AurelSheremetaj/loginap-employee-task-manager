from  model import Employee
import random
 
class EmployeeManagerController:
    
    def add_employee(self,department,employment_data):
        employees = department.employee_list
        unique_id = random.randint(1,1000)
        new_employee = Employee(unique_id,employment_data[0],employment_data[1],employment_data[2],employment_data[3],[])
        employees.append(new_employee)
        return new_employee
    
    #TODO
    
    def delete_employee(self,department,employee_data):
        employees = department.employee_list
        
        
        for employee in employees:
            if employee.name == employee_data[0]:
                employees.remove(employee) 
    
    
    def _update_employee(self,department,employee_id,updated_employee_data):
        for employee in department.employee_list:
            if employee.id == employee_id:
                employee.name = updated_employee_data[0]
                employee.address = updated_employee_data[1]
                employee.email = updated_employee_data[2]
                employee.phone_number = updated_employee_data[3]
                break
                