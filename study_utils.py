import json

def calculate_total(study_dict):
    total = 0

    for day, time in study_dict.items():
        total += time
    return total

def find_long_study_days(study_dict):
    long_days = []
    for day, time in study_dict.items():
        if time >= 60:
            long_days.append(day)
    return long_days

def calculate_average(study_dict):
    total = calculate_total(study_dict)
    if len(study_dict) == 0:
        return 0
    average = total / len(study_dict)
    return average

def add_study_record(study_data):
    date = input("Enter date (YYYY-MM-DD): ")

    if date in study_data:
        print("This date already exists.")
        return

    try:
        minutes = int(input("Enter study time (minutes): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if minutes < 0:
        print("Study time cannot be negative.")
        return
    study_data[date] = minutes


def save_study_data(study_data, file_path):
    with open(file_path, "w") as file:
        json.dump(study_data, file, indent=4)

