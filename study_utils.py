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