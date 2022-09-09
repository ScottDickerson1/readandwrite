# using the file steps.csv, calculate the average steps taken each month. Each row represents one day. 
# Output should have the name of the month and the corresponding average steps for that month (such as 'January, 5246.19')

import csv

infile = open('steps.csv', 'r')
csvfile = csv.reader(infile, delimiter=',')

outfile = open('avg_steps.csv', 'w')

month = 1

next(csvfile)
while month <= 12:
    steps = 0
    count = 0
    for record in csvfile:
        if int(record[0]) == month:
            steps += int(record[1])
            count += 1
            average = round(steps / count, 2)
            months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            month_name = months[month-1]
            outfile.write(month_name + ', ' + str(average) + '\n')
            month += 1

infile.close()
outfile.close()


