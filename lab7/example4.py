name = []
salary = []
for i in range(5):
  employee = input("Enter the employee's name and salary by splitting with (,): ").split(",")
  name.append(employee[0])
  salary.append(employee[1])
employees = list(zip(name, salary))
employees = dict(employees)
