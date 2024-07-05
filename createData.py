import csv
input = open('Final Project/lyrics-data.csv', 'rb')
output = open('lyrics-data-edit.csv', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
    if row[4]=='en':
        writer.writerow(row)
input.close()
output.close()