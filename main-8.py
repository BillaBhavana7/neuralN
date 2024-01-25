class Employee:
  employee_count = 0

  def __init__(self, name, family, salary, department):
      self.name = name
      self.family = family
      self.salary = salary
      self.department = department

      Employee.employee_count += 1

  def average_salary(self, *salaries):
      total_salary = sum(salaries)
      return total_salary / len(salaries) if len(salaries) > 0 else 0

class FulltimeEmployee(Employee):
  def __init__(self, name, family, salary, department, working_hours):
      super().__init__(name, family, salary, department)

      self.working_hours = working_hours

employee1 = Employee("Bhavana", "Family1", 50000, "SE1")
employee2 = Employee("Vaishnavi", "Family2", 50000, "ASE")

fulltime_employee = FulltimeEmployee("Vinnu", "Family3", 50000, "IT", 38)

average_salary_all = employee1.average_salary(employee1.salary, employee2.salary)
average_salary_fulltime = fulltime_employee.average_salary(fulltime_employee.salary)

# Print results
print("Total Employees:", Employee.employee_count)
print("Average Salary of all Employees:", average_salary_all)
print("Average Salary of Fulltime Employee:", average_salary_fulltime)
