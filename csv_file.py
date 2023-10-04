# how to work with csv files

import csv

### WRITE (override if exists one)
f = open("new_csv.csv", mode="w", newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(['1', '2', '3'])
f.close()

### APPEND
f = open ("new_csv.csv", mode= "a")
csv_append = csv.writer(f)
csv_append.writerows([['4', '5', '6'], ['7', '8', '9']])
f.close()

### READ
f = open("new_csv.csv", mode="r", encoding="utf-8")
csv_reader = csv.reader(f)
print (list(csv_reader))
