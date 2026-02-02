from kivy.uix.gridlayout import GridLayout
from dataprovider import DataProvider
from kivymd.uix.textfield import MDTextField
from kivy.uix.button import Button
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from admin_controller import EmployeeManagerController
from model import Employee
from kivy.uix.popup import Popup
from database_controller import EmployeeDatabaseManager

class EmployeeManagerContentPanel:
    
    
    
    def __init__(self):
        self.selected_row = -1
        #self.department_list = DataProvider().department_list
        self.employee_database_manager = EmployeeDatabaseManager("employee-app", "postgres" ,"2003","localhost",2022)
        self.department_list = self.employee_database_manager.get_department_list()
        self.employee_manager_controller = EmployeeManagerController()
        if self.department_list:
            self.selected_department = self.department_list[0]
            if self.selected_department.employee_list:
                self.selected_employee = self.selected_department.employee_list[0]
            else:
                self.selected_employee = None
        else:
            self.selected_department = None
            self.selected_employee = None
        
    
    
    def create_content_panel(self):
        split_layout_panel = GridLayout(cols=2)
        split_layout_panel.add_widget(self._create_employee_input_data_panel())
        split_layout_panel.add_widget(self._create_employee_management_panel())
        return split_layout_panel
    
    def _create_employee_input_data_panel(self):
        input_data_component_panel =GridLayout(cols=1,padding = 30,spacing = 20)
        input_data_component_panel.size_hint_x = None
        input_data_component_panel.width = 400
        
        self.name_input = MDTextField(multiline = True,font_size = '18sp',hint_text = 'Name')
        input_data_component_panel.add_widget(self.name_input)
    
        self.address_input = MDTextField(multiline = False,font_size = '18sp',hint_text = 'Address')
        input_data_component_panel.add_widget(self.address_input)
        
        self.email_input = MDTextField(multiline = False,font_size = '18sp',hint_text = 'Email')
        input_data_component_panel.add_widget(self.email_input)
        
        self.phone_nr_input = MDTextField(multiline = False,font_size = '18sp',hint_text = 'Phone number')
        input_data_component_panel.add_widget(self.phone_nr_input)
        
        input_data_component_panel.add_widget(self._create_buttons_component_panel())
        
        return input_data_component_panel
    
    
    def _create_employee_management_panel(self):
        content_panel  = GridLayout(cols=1,spacing = 10)
        content_panel.add_widget(self._create_department_selector())
        content_panel.size_hint_x = None
        content_panel.width = 1200
        content_panel.add_widget(self._create_employee_table_panel())
        return content_panel
    
    
    def _create_buttons_component_panel(self):
        buttons_component_panel = GridLayout(cols=3,padding = 0,spacing = 20)
        add_button = Button(text = 'Add',size_hint=(None,None),size = (100,40),background_color = (0,1,1,1))
        update_button = Button(text = 'Update',size_hint=(None,None),size=(100,40),background_color = (0,1,1,1))
        delete_button = Button(text = 'Delete',size_hint = (None,None),size = (100,40),background_color = (0,1,1,1))
       
       
        add_button.bind(on_press = self.add_employee)
        update_button.bind(on_press = self.update_employee)
        delete_button.bind(on_press = self._delete_employee)
       
        buttons_component_panel.add_widget(add_button)
        buttons_component_panel.add_widget(update_button)
        buttons_component_panel.add_widget(delete_button)
        
        return buttons_component_panel
    
    
    def _create_employee_table_panel(self):
        table_panel = GridLayout(cols = 1,padding = 10,spacing = 0)
        self.employee_table = self.create_employee_table()
        
        #self.employee_table.bind(on_check_press = self._checked)
        self.employee_table.bind(on_row_press =self._on_row_press)
                
        table_panel.add_widget(self.employee_table)
        return table_panel
    
    def _create_department_selector(self):
        button = Button(text='Select a department',size_hint = (1,0.1),background_color=(0,1,1,1))
        button.bind(on_release = self.open_department_dropdown)
        return button
    
    
    def  create_employee_table(self):
        table_row_data = []

        #self.selected_department = self.department_list[0]

        if self.selected_department:
            employees = self.selected_department.employee_list
        else:
            employees = []

        for employee in employees:
            table_row_data.append(( employee.name, employee.address, employee.email, employee.phone_nr))
            
        self.employee_table = MDDataTable(
            pos_hint = {'center_x' : 0.5, 'center_y': 0.5},
            check = True,
            use_pagination = True,
            rows_num = 10,
            column_data = [
                #("ID",dp(40)),
                ("Name", dp(40)),
                ("Address",dp(30)),
                ("Email",dp(40)),
                ("Phone Nr",dp(25))
            ],
            row_data = table_row_data,
            background_color_selected_cell = (0,1,1,0.5)
        )
        return self.employee_table
    
    def open_department_dropdown(self,button):
        menu_items = []
        department_list = self.department_list
        
        for department in department_list:
            menu_items.append({
                "view class": "OneLineListItem",
                "text" : department.name,
                "on_release": lambda d=department: self._on_department_selection(d)
            })
        self.department_dropdown = MDDropdownMenu( 
            caller = button,
            items = menu_items,
            width_mult= 5,
            max_height = dp(150),
            
        )
        self.department_dropdown.open()
        
    def _on_department_selection(self,department):
        self.selected_department = department
        employee_list = department.employee_list
        table_row_data = []
        for employee in employee_list :
            table_row_data.append(( employee.name, employee.address, employee.email, employee.phone_nr))
            self.employee_table.row_data = table_row_data
            self.department_dropdown.dismiss()
        
        
        
    #def _checked(self,instance_table,current_row):
     #   self.selected_employee = Employee(current_row[0],current_row[1],current_row[2],current_row[3],current_row[4],[])
        
      #  self.name_input.text = self.selected_employee.name
       # self.address_input.text = self.selected_employee.address
        #self.email_input.text = self.selected_employee.email
        #self.phone_nr_input.text = self.selected_employee.phone_nr       
        
        
    def _on_row_press(self,instance,row):
        self.selected_row = int(row.index / len(instance.column_data))
        if self.selected_department and 0 <= self.selected_row < len(self.selected_department.employee_list):
            self.selected_employee = self.selected_department.employee_list[self.selected_row]
            print("Selected employee :" + self.selected_employee.name)

            self.name_input.text = self.selected_employee.name
            self.address_input.text = self.selected_employee.address
            self.email_input.text = self.selected_employee.email
            self.phone_nr_input.text = self.selected_employee.phone_nr
    
    def add_employee(self,instance):
        name = self.name_input.text
        address = self.address_input.text
        email = self.email_input.text
        phone_nr = self.phone_nr_input.text

        employee_data = []

        employee_data.append(name)
        employee_data.append(address)
        employee_data.append(email)
        employee_data.append(phone_nr)

        if self._is_data_valid(employee_data):
            department_id = self.selected_department.id
            self.employee_database_manager.add_employee(
                department_id, employee_data
            )
            # Refresh the employee list from DB
            self.selected_department.employee_list = self.employee_database_manager.get_employees_by_department_id(department_id)
            self.update_employee_table_data(self.selected_department.employee_list)
            self._clear_input_text_field()
        else:
            popup = Popup(
                title= "Invalid data",
                content = Label(text = "Provide mandatory data to add a new Employee"),
                size_hint = (None,None),
                size = (400,200)
            )
            popup.open()
    
    
    def update_employee(self,instance):
        if self.selected_row != -1:
           
            employee_update_data = []
            employee_update_data.append(self.name_input.text)
            employee_update_data.append(self.address_input.text)
            employee_update_data.append(self.email_input.text)
            employee_update_data.append(self.phone_nr_input.text)
            if self._is_data_valid(employee_update_data):
                #self.employee_manager_controller._update_employee(self.selected_department,int(self.selected_employee.id),employee_data)
                employee_to_update = self.selected_employee
                
                employee_to_update.name = self.name_input.text
                employee_to_update.address = self.address_input.text
                employee_to_update.email = self.email_input.text
                employee_to_update.phone_nr = self.phone_nr_input.text
                self.employee_database_manager.update_employee(employee_to_update)
            
        #table_row_data = []
    
        #employee_list = self.selected_department.employee_list
        
        #for employee in employee_list:
         #   table_row_data.append(( employee.name, employee.address, employee.email, employee.phone_nr))   
        #self.employee_table.row_data = table_row_data 
    
        self.update_employee_table_data(self.selected_department.employee_list)
    def update_employee_table_data(self,employee_model_data):
        self.employee_table_data = []
        for employee in employee_model_data:
            self.employee_table_data.append(
                ( employee.name, employee.address, employee.email, employee.phone_nr)
            )
            self.employee_table.row_data = self.employee_table_data
    
    
    def _delete_employee(self,instance):

        if self.selected_row != -1 and self.selected_employee is not None:
            #employee_to_remove = self.employee_table.row_data[self.selected_row]
            employee_to_remove = self.selected_employee

            #del self.employee_table.row_data[self.selected_row]
            self.employee_database_manager.delete_employee(employee_to_remove)
            # Refresh the employee list from DB
            self.selected_department.employee_list = self.employee_database_manager.get_employees_by_department_id(self.selected_department.id)
            self.update_employee_table_data(self.selected_department.employee_list)
            self.selected_employee = None
            self.selected_row = -1

            self._clear_input_text_field()
        else:
            popup = Popup(
                title= "Invalid data",
                content = Label(text = "Select any row to delete"),
                size_hint = (None,None),
                size = (400,200)
            )
            popup.open()
            
            
            
    def _is_data_valid(self,employee_data):
        return (
            employee_data[0] != ""
            and employee_data[1] != ""
            and employee_data[2] != ""
            and employee_data[3] != ""
        )     
    
    def _clear_input_text_field(self):
        self.name_input.text = ""
        self.address_input.text = ""
        self.email_input.text = ""
        self.phone_nr_input.text = ""
    
class TaskManagerContentPanel:
    
    def __init__(self):
    
        self.department_list =DataProvider().department_list
        self.selected_department = self.department_list[0]
        self.selected_employee = self.selected_department.employee_list[0]
        self.employee_dropdown_selection_item  = []
        
    
    def create_content_panel(self):
        split_layout_panel = GridLayout(cols =2)
        split_layout_panel.add_widget(self._create_task_input_data_panel())
        split_layout_panel.add_widget(self._create_management_panel())
        return split_layout_panel
    
    def _create_task_input_data_panel(self):
        input_data_component_panel = GridLayout(cols = 1,padding = 30,spacing = 20)
        input_data_component_panel.size_hint_x = None
        input_data_component_panel.width = 400
        
        self.name_input = MDTextField(multiline = True,font_size = '18sp',hint_text = 'Name')
        input_data_component_panel.add_widget(self.name_input)
        self.description_input = MDTextField(multiline = True,font_size = '18sp',hint_text = 'Description')
        input_data_component_panel.add_widget(self.description_input)
        input_data_component_panel.add_widget(self._create_priority_input_data_panel())
        input_data_component_panel.add_widget(self._create_button_component_panel())
        return input_data_component_panel
    
    
    def _create_priority_input_data_panel(self):
        priority_input_panel = GridLayout(cols=2,spacing = 20)
        priority_input_panel.size_hint = (None,None)
        priority_options =["Low","Medium","High"]
        
        for priority in priority_options:
            checkbox = CheckBox(group= 'pririty',active = False,color = (0,0,0,1))
            checkbox_label = Label(text = priority,color = (0,0,0,1))
            priority_input_panel.add_widget(checkbox)
            priority_input_panel.add_widget(checkbox_label)
            
        return priority_input_panel
        
        
    def _create_management_panel(self):
        content_panel = GridLayout(cols=1,spacing = 20)
        content_panel.size_hint_x = None
        content_panel.width = 1200 
        content_panel.add_widget(self._create_department_dropdown())
        content_panel.add_widget(self._create_employee_dropdown())
        content_panel.add_widget(self._create_table())
        return content_panel
    
    def _create_button_component_panel(self):
        buttons_component_panel = GridLayout(cols = 3,spacing = 10,padding =0)
        add_button = Button(text = 'Add',size_hint = (None,None),size= (100,40),background_color = (0,1,1,1))
        update_button = Button(text = 'Update',size_hint = (None,None),size= (100,40),background_color = (0,1,1,1))
        delete_button = Button(text = 'Delete',size_hint = (None,None),size= (100,40),background_color = (0,1,1,1))
        buttons_component_panel.add_widget(add_button)
        buttons_component_panel.add_widget(update_button)
        buttons_component_panel.add_widget(delete_button)
        return buttons_component_panel
    
    
    def _create_department_dropdown(self):
        button  = Button(text = 'Select  a department',size_hint = (1,0.1),background_color = (0,1,1,1))
        button.bind(on_release = self._open_department_dropdown)
        return button
    
    def _open_department_dropdown(self,button):
        menu_items = []
        department_list = self.department_list
        for department in department_list:
            menu_items.append(
                {
                    "viewclass":"OneLineListItem",
                    "text": department.name,
                    "on_release" : lambda d=department: self.on_department_selection(d)
                    }
                )
            
        self.department_dropdown = MDDropdownMenu( 
        caller = button,
        items = menu_items,
        width_mult = 5,
        max_height = dp(150)
        )
        self.department_dropdown.open()
        
    def on_department_selection(self,department):
        self.selected_department = department
        employee_list = department.employee_list
        for employee in employee_list:
            self.employee_dropdown_selection_item.append(
                {
                    "viewclass":"OneLineListItem",
                    "text": employee.name,
                    "on_release" : lambda e=employee: self.on_employee_selection(e)
                }
                
            )
            self.department_dropdown.dismiss()
        
    def _create_employee_dropdown(self):
        button  = Button(text = 'Select  an employee',size_hint = (1,0.1),background_color = (0,1,1,1))
        button.bind(on_release = self._open_employee_dropdown)
        return button
    
    def _open_employee_dropdown(self,button):
        self.employee_dropdow_selection_items = []
        department_list = self.department_list
        employee_list = self.selected_department.employee_list
        for employee in employee_list:
            self.employee_dropdow_selection_items.append(
                {
                    "viewclass":"OneLineListItem",
                    "text": employee.name,
                    "on_release" : lambda e=employee: self.on_employee_selection(e)
                    
                    }
                )
            
        self.employee_dropdown = MDDropdownMenu( 
        caller = button,
        items = self.employee_dropdow_selection_items,
        width_mult = 5,
        max_height = dp(150)
        )
        self.employee_dropdown.open()
        
    def on_employee_selection(self,employee): 
        self.selected_employee = employee
        table_row_data = []
        task_list = employee.task_list
        for task in task_list:
            table_row_data.append((task.name,task.description,task.priority.value))
        self.task_table.row_data = table_row_data
        self.employee_dropdown.dismiss()
                
    def _create_table(self):
        table_row_data = []
        
        self.department = self.department_list[0]
        employees = self.department.employee_list
        task_list = employees[0].task_list
        
        for task in task_list:
            # fixed curly bracket by using normal brackets for table row data
            table_row_data.append((task.name, task.description, task.priority.value))
            
        # CTRL plus G eshte per Go To Line
        self.task_table = MDDataTable(
            pos_hint = {'center_x': 0.5 ,'center_y': 0.5},
            check = True,
            use_pagination = True,
            rows_num = 10,
            column_data = [
                ("Name",dp(40)),
                ("Description",dp(50)),
                ("Priority",dp(40))
            ],
            row_data = table_row_data
        
        )
        return self.task_table    