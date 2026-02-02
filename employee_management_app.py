from dataprovider import DataProvider

class DepartmentEmployeeManagementApp:
    def start(self):
        self.department_list = []
        self.data_provider = DataProvider()
        self.department_list = self.data_provider.department_list
        
        for department in self.department_list:
            print("==============================================================")
            print("List of employees in the " + department.name + " department")
            print("==============================================================")
            
            for employee in department.employee_list:
                print(employee.name + ", " + employee.address + ", " + employee.email + ", " + employee.phone_nr)
                print("-------------------------------------------------------------")
                
                for task in employee.task_list:
                    print(task.name + ", " + task.description + ", " + task.priority.value)
                print("---------------------------------------------------------------")
                
employee_management_app = DepartmentEmployeeManagementApp()
employee_management_app.start()