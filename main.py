import study_utils as su
from pathlib import Path
import json

file_path = Path(__file__).parent / "study_data.json"
try:
    with open(file_path, "r") as file:
        study_data = json.load(file)
except FileNotFoundError:
    print("wrong file")

else:
    print("===== Study Manager =====")
    print("")
    print("1. View study statistics")
    print("2. Add study record")
    print("3. Exit")
    print("")
    print("")
    try:
        option = int(input("choose an option: "))
    except ValueError:
        print("wrong form.")


    else:
        if option == 1:
            total = su.calculate_total(study_data)
            average = su.calculate_average(study_data)
            long = su.find_long_study_days(study_data)
            
            
            print("===== Study Tracker v2 ======")
            print("")
            print(f"Total: {total} minutes")
            print(f"Average: {average} minutes")
            print(f"Long study days: {long}")


        elif option == 2:
            su.add_study_record(study_data)
            su.save_study_data(study_data, file_path)


        elif option == 3:
            pirnt("good bye!")
        else:
            print("worng number.")

