import csv


with open ("rows.txt", "rt") as f:
    reader = csv.reader(f, delimiter='\t', skipinitialspace=True)
    lineDif = list()

    for line in reader:
        line = list(map(int, line))
        # print(line)
        diff = max(line) - min(line)
        # print(diff)
        lineDif.append(diff)
        # print(lineDif)

    print(lineDif)
    controlSum = sum(lineDif)
    print(controlSum)
