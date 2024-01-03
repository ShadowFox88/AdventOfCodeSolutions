def get_data(day: int):
    # Get the content of every line from the data.txt file
    with open(f"Data_Files/2023/Day_{day}/input.txt", "r") as f:
        data = f.read().splitlines()

    return data
