import csv

infile = open("customers.csv", "r")
outfile = open("customer_country.csv", "w")

line = csv.reader(infile, delimiter=",")

next(infile)

outfile.write("First Name Last name, Country\n")

for record in line:

    first = record[1]
    last = record[2]
    country = record[3]
    newfile = first + " " + last + ", \t\t" + country
    outfile.write(newfile + "\n")

infile.close
outfile.close
