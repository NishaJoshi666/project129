import csv

dataset1 = []
data = []
with open('dataset_1.csv','r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

dataset2 = []
with open('datasetsorted.csv','r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)


header1 = dataset1[0]
planetdata1 = dataset1[1:]

header2 = dataset2[0]
planetdata2 = dataset2[1:]
planetdata = []

headers = header1+header2

for index,datarow in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])

planetdata.sort(key=lambda planetdata:planetdata[2])

with open('final.csv','a+') as f1:
    csvwriter = csv.writer(f1)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)