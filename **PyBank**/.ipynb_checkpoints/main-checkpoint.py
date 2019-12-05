import os
import csv

dataPath = os.path.join('.','Resources','budget_data.csv')

with open(dataPath, 'r') as csvfile:
    text = csvfile.read()
    print(text)

    rows = text.split("\n")
    print (rows)

    table = rows.map(lambda row: row.split(","))
    print(table)