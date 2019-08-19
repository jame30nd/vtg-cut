import csv
# import RPi.GPIO
reader = csv.reader(
    open("csvfile.csv"), delimiter=";")
included_cols = [22]
count = 0
content = []
for row in reader:
    # content = list(row[i] for i in included_cols)
    content.append(row[22])
    # print()
    #
num_list = len(content)
num_list_target = num_list - 1
print(content[num_list_target-1])
# num = content.index()
# if count == 12:
#     print(row[22])
# count += 1
