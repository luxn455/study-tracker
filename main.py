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
    total = su.calculate_total(study_data)
    average = su.calculate_average(study_data)
    long = su.find_long_study_days(study_data)

    print("===== Study Tracker v2 ======")
    print("")
    print(f"Total: {total} minutes")
    print(f"Average: {average} minutes")
    print(f"Long study days: {long}")
