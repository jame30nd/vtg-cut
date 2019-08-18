import csv
# import RPi.GPIO
import pandas
reader = csv.reader(
    open("csvfile.csv"), delimiter=";")


for row in reader:
    print(row[0])
