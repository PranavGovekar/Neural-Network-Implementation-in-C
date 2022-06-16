import csv
file = open(".\\20-10\\layer_1_weights.csv")
csvreader = csv.reader(file)

string = "{"

rows = []
for row in csvreader:
    string = string + "{"
    for num in row:
        string = string + " " + str(num) + ","
    string = string + "}\n"

string = string + "}"

file = open(".\\20-10 weights\\layer_1_weights.txt", "w")
file.write(string)
