import csv
with open('data.csv', newline='') as f:
    rd = csv.reader(f)
    for row in rd:
        print(row)
