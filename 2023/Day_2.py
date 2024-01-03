import json


with open("Data_Files/2023/Day_2/input.txt", "r") as f:
    data = f.read().splitlines()

def convert_data(data: str):
    temp = data.split(":")
    temp = [i.split() for i in temp]
    game_number = int(temp[0][-1])

    games = []

    data = data.replace(f"Game {game_number}: ", "")

    temp = data.split(";")

    for i in temp:
        temp2 = i.split(" ")
        temp2 = [j for j in temp2 if j]
        counter = {
            "Green": 0,
            "Blue": 0,
            "Red": 0
        }
        for count, j in enumerate(temp2):
            if count % 2 == 0:
                match temp2[count + 1].strip(","):
                    case "green":
                        counter["Green"] = int(j)
                    case "blue":
                        counter["Blue"] = int(j)
                    case "red":
                        counter["Red"] = int(j)
        games.append(counter)

    return {
        "Game_Number": game_number,
        "Actions": games
    }

results = []
total = 0
already_counted = []

for i in data:
    #print(convert_data(i))
    results.append(convert_data(i))

# results = [convert_data(data[4])]

for i in results:
    for j in i["Actions"]:
        if i["Game_Number"] not in already_counted:
            if j["Blue"] > 14:
                already_counted.append(i["Game_Number"])
                total += i["Game_Number"]
            elif j["Red"] > 12:
                already_counted.append(i["Game_Number"])
                total += i["Game_Number"]
            elif j["Green"] > 13:
                already_counted.append(i["Game_Number"])
                total += i["Game_Number"]

print(5050 - total)

total = 0

for i in results:
    green = 0
    red = 0
    blue = 0
    for j in i["Actions"]:
        green = max(j["Green"], green)
        blue = max(j["Blue"], blue)
        red = max(j["Red"], red)

    total += green * red * blue

print(total)