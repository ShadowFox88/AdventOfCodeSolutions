import time

# Get the content of every line from the data.txt file
with open("Data_Files/2023/Day_1/input.txt", "r") as f:
    input1 = f.read()
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


#print(convert_text_digits_to_int(data))

def nithi(input1):
    input1 = input1.replace("zero","0o").replace("one","o1e").replace("two","t2o").replace("three","t3e").replace("four","4").replace("five","5e").replace("six","6").replace("seven","7n").replace("eight","e8t").replace("nine","n9e")
    array = input1.split()
    total = 0
    num1=""
    num2=""

    for str in array:
        for char in str:
            if char.isnumeric():
                num1 = char
                break
        for char in reversed(str):
            if char.isnumeric():
                num2 = char
                break
    total = total + int(num1+num2)


n = 10000

start_nithi = time.time()
for i in range(n):
    nithi(input1)

end_nithi = time.time()

start_me = time.time()
for i in range(n):
    convert_text_digits_to_int(data)

end_me = time.time()

if end_nithi - start_nithi > end_me - start_me:
    print("I am faster")
elif end_nithi - start_nithi < end_me - start_me:
    print("Nithi is faster")
else:
    print("Tie.")

print(f"Me: {end_me - start_me}")
print(f"Nithi: {end_nithi - start_nithi}")