import csv
from email.mime import base

infile = open('EmployeePay.csv', 'r')
csvfile = csv.reader(infile, delimiter=',')

next(csvfile)

for record in csvfile:
    emp_id = str(record[0])
    fname = str(record[1])
    lname = str(record[2])
    salary = float(record[3])
    bonus = float(record[4])
    total_comp = salary + bonus

    print('Employee ID: ', emp_id)
    print('First Name: ', fname)
    print('Last Name: ', lname)
    print('Total Compensation: ' + str(total_comp))
    input()

infile.close()
