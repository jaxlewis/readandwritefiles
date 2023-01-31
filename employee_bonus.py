import csv

employee = open("EmployeePay.csv", "r")

employee_file = csv.reader(employee, delimiter=",")

next(employee_file)

for record in employee_file:

    print("ID:", record[0])
    print("First name:", record[1])
    print("Last name:", record[2])
    print("Salary:", record[3])
    print("Bonus:", record[4])
    print("___________________________")

employee.close()
