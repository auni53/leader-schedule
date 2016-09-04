import json

def do(filename):
    with open(filename) as file:
        data = {}
        raw = file.readlines()
        for line in raw[1:]:
            items = line.strip().split(",")
            if items[0] != "":
                colour = items[0].lower()

                c = 0
                for event in items:
                    if (c > 0 and event == ''):
                        items[c] = items[c - 1]
                    c += 1

                data[colour] = items[1:]
    return data
 
if __name__ == "__main__":
    with open("data.json", "w") as file:
        for day in ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]:
            raw_dict = do((day + ".csv"))
            file.write(day[0:3] + ": ")
            file.write(json.dumps(raw_dict))
            file.write(",\n")
