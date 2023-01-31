import csv

sales = open("sales.csv", "r")
report = open("salesreport.csv", "w")
line = csv.reader(sales, delimiter=",")
next(sales)

cust_ID = "250"
cust_total = 0
report.write("Customer\t|\tTotal\n")
for record in line:
    if cust_ID != record[0]:
        report.write(cust_ID + "\t\t\t\t" + str("%.2f" % cust_total) + "\n")
        cust_ID = record[0]
        cust_total = 0

    add = float(record[3]) + float(record[4]) + float(record[5])
    cust_total += add

report.write(cust_ID + "\t\t\t\t" + str("%.2f" % cust_total))

sales.close()
report.close()
