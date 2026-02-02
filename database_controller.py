import psycopg2
from model import Department,Employee

class EmployeeDatabaseManager:
    def __init__(self,database_name,user,password,host,port):
        self.connection = psycopg2.connect(
            dbname=database_name,
            user = user,
            password = password,
            host = host,
            port = port
        )
        
        print("Database created successfully")
        
        self.cursor = self.connection.cursor()
        self.create_department_database_table()
        
        self.add_departments()
        
    def create_department_database_table(self):
        query = "CREATE TABLE IF NOT EXISTS departments (id UUID PRIMARY KEY DEFAULT gen_random_uuid(), name VARCHAR(20))"
        self.execute_query(query)
        
        create_employee_table_query = "CREATE TABLE IF NOT EXISTS employees (id UUID PRIMARY KEY DEFAULT gen_random_uuid(), name VARCHAR(50),address VARCHAR(50), email VARCHAR (50), phone_nr VARCHAR(50) , department_id UUID REFERENCES departments(id) )"
        self.execute_query(create_employee_table_query)
        
    def add_departments(self):
        department_list = [ "Sale" , "Marketing", "Development"]
        for department in department_list:
            self.add_department(department)
            
    def add_department(self,department_name):
        select_department_query = (f"Select Id from departments where name = '{department_name}'")
        self.cursor.execute(select_department_query)
        department_result = self.cursor.fetchone()
        
        if department_result:
            print("Department already exists")
            
        else:
            query = f"INSERT INTO departments (name) VALUES ('{department_name}')"
            self.execute_query(query)
            print("Department created successfully")
        
        
        
    def get_department_list(self):
        select_department_query = "SELECT * FROM departments"
        self.cursor.execute(select_department_query)
        department_results = self.cursor.fetchall()
        department_list = []
        for department in department_results:
            employee_list = self.get_employees_by_department_id(department[0])
            department_list.append(Department(department[0],department[1],employee_list))
        return department_list
            
        
    def execute_query(self,query):
        self.cursor.execute(query)
        self.connection.commit()
        
        
    def add_employee(self,department_id,employee_data):
        #select_department_query = f"Select ID from departments where name = '{department.name}'"
        #self.cursor.execute(select_department_query)
        #department_result = self.cursor.fetchone()
        
        #if department_result:
         #   department_id  = department_result[0]
            
          #  insert_employee_query = f"INSERT INTO employees (name,address,email,phone_nr,department_id) VALUES ( '{employee_data[0]}','{employee_data[1]}', '{employee_data[2]}','{employee_data[3]}', '{department_id}')"
           # self.execute_query(insert_employee_query)
        #else:
         #   raise Exception("Department not found! Deparment name:" + department.name) 
        if department_id and department_id != '' :   
            insert_employee_query = f"INSERT INTO employees (name,address,email,phone_nr,department_id) VALUES ( '{employee_data[0]}','{employee_data[1]}', '{employee_data[2]}','{employee_data[3]}', '{department_id}')"
            self.execute_query(insert_employee_query)
        else:
            raise Exception ("Department Id is missing or empty")
            
    def get_employees_by_department_id(self,department_id):
        select_employee_query = (
            f"SELECT * FROM employees WHERE department_id = '{department_id}'"
        )
        self.cursor.execute(select_employee_query)
        employee_data  = self.cursor.fetchall()
        
        employee_list = []
        for employee in employee_data:
            employee_list.append(Employee(employee[0],employee[1],employee[2],employee[3],employee[4] ,[]))
        return employee_list

    def update_employee(self,employee_to_update):
        if employee_to_update.id and employee_to_update.id != '':
            update_employee_query = f"UPDATE employees SET name = '{employee_to_update.name}',address  ='{employee_to_update.address}',email = '{employee_to_update.email}',phone_nr = '{employee_to_update.phone_nr}' WHERE id = '{employee_to_update.id}'"
            self.execute_query(update_employee_query)
        else:
            raise Exception("Employee Id is missing or empty")
        
    def delete_employee(self,employee_to_delete):
        if employee_to_delete.id and employee_to_delete.id != '':
            delete_employee_query = f"DELETE FROM employees WHERE id = '{employee_to_delete.id}'"
            self.execute_query(delete_employee_query)
        else:
            raise Exception ("Employee ID is missing or empty")