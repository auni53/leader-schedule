import csv

def do(filename):
    with open(filename) as file:
        data = {}
        raw = file.readlines()
        for line in raw[1:]:
            items = line.strip().split(",")
            colour = items[0]
            data[colour] = items[1:]
    return data
 
if __name__ == "__main__":
    for day in ["monday.csv", "tuesday.csv", "wednesday.csv", "thursday.csv", "friday.csv"]:
        print(do(day))
