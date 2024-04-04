"""
    Exercise1: Write a Python class Employee with attributees like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
                Sample Employee Data:
                "ADAMS","E7876", 5000, "ACCOUNTING"
                "JONES", "E7499", 45000, "RESEARCH"
                "MARTIN","E7900", 50000, "SALES"
                "SMITH", "E7689", 55000, "OPERATIONS"
                
            -Use "assign_department" method to change the department of an employee
            -Use "print employee details" method to print the details of an employee 
            -Use "calculate_emp_salary" method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to salary. Overtime is calculated as following formula: 
                overtime = hour_worked - 50
                Overtime amount = (overtime * (salary/50))               

"""

class Employee : 
    def __init__(self, name , emp_id, salary, department): 
        self.name = name 
        self.id  = emp_id 
        self.salary = salary
        self.department  = department 
        
    def calculate_salary(self, salary, hours_worked):
        overtime = 0 
        if hours_worked > 50 : 
            overtime = hours_worked - 50
        self.salary  += (overtime * (self.salary / 50))
        
    def assing_department_details(self, emp_department): 
        self.department  = emp_department  
        
    def print_employee_details (self) : 
        print(" ")
        print("Name       : ",self.name)
        print("ID         : ",self.id)
        print("Salary     : ",self.salary)
        print("Department : ", self.department)
        print("--------------------------------------------")
        
        
employee1 = Employee("ADAMS","E7876", 5000, "ACCOUNTING")
employee2 = Employee("JONES", "E7499", 45000, "RESEARCH")
employee3 = Employee( "MARTIN","E7900", 50000, "SALES")

print("==>Original Employee Details: ")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()

# Change the department of employee1 and employee3
employee1.assing_department_details("OPERATIONS")
employee2.assing_department_details("SALES")

# Now calculate the overtime of the employee who are eligible: 
employee2.calculate_salary(45000, 52)  # JONES is working 52 h
employee3.calculate_salary(45000, 60)  # MARTIN is working 60 h 

print("==>Updated Employee Details: ")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()