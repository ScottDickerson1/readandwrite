import csv

infile = open('customers.csv', 'r')

outfile = open('customer_country.csv', 'w')

csvfile = csv.reader(infile, delimiter = ',')

i = 1
next(csvfile)
for record in csvfile:
    name = str(record[1] + ' ' + record[2])
    country = str(record[4])
    outfile.write('Name: ' + name + ' Country: ' + country + '\n')
    i += 1

outfile.write('Total Number of Customers: ' + str(i))

print()
print('Total Number of Customers: ', i)


infile.close()
outfile.close()


