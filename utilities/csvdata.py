import csv

def getCsvData(fileName):
    rows = []

    datafile = open(fileName, mode="r")

    reader = csv.reader(datafile)

    next(reader)

    for row in reader:
        rows.append(row)

    return rows