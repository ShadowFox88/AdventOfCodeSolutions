import time

# Get the content of every line from the data.txt file
with open("Data_Files/2023/Day_1/input.txt", "r") as f:
    data = f.read().splitlines()

# Part 1

def extract_numbers(data):
    # Extract all of the numbers from each string in data
    numbers = [[j for j in i if j.isnumeric()] for i in data]

    # Get the calibration value per line - the first and last digit
    numbers = [int(i[0] + i[-1]) for i in numbers]

    # Get the sum of all of the calibration values
    return sum(numbers)

# Part 2
    
def convert_text_digits_to_int(data):
    spelled_numbers = {
        "one": "o1ne",
        "two": "t2wo",
        "three": "th3ree",
        "four": "fo4ur",
        "five": "fi5ve",
        "six": "si6x",
        "seven": "se7ven",
        "eight": "eig8ht",
        "nine": "ni9ne"
    }

    for i in spelled_numbers.keys():
        data = [j.replace(i, spelled_numbers[i]) for j in data]

    return extract_numbers(data)

t0 = time.time()
print(convert_text_digits_to_int(data))
t1 = time.time()

print(t1-t0)