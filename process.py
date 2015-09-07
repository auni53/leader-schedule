import json

def do(filename):
    with open(filename) as file:
        data = {}
        raw = file.readlines()
        for line in raw[1:-1]:
            items = line.strip().split(",")
            if items[0] != "":
                colour = items[0]
                data[colour] = items[1:-1]
    return data
 
if __name__ == "__main__":
    with open("data.json", "w") as file:
        for day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
            raw_dict = do((day + ".csv"))
            file.write(json.dumps(raw_dict))
            file.write("\n")
