"""
My data.py file is currently formatted like this:

activities = {
    'Monday\n01/01/2023': [("Breakfast", 1), ("Gaming", 22), ("Sleep", 1)],
    'Tuesday\n02/01/2023': [("Study", 19), ("Lunch", 1), ("Sleep", 4)],
    'Wednesday\n03/01/2023': [("Study", 10), ("Lunch", 10), ("Sleep", 4)],
    'Thursday\n04/01/2023': [("Study", 5), ("Bike", 15), ("Sleep", 4)],
}

however, after doing this for weeks, there isn't enough space for all the labels to fit, so this program formats the data like this:

activities = {
    '01/01/2023': [("Breakfast", 1), ("Gaming", 22), ("Sleep", 1)],
    '02/01/2023'': [("Study", 19), ("Lunch", 1), ("Sleep", 4)],
    '03/01/2023': [("Study", 10), ("Lunch", 10), ("Sleep", 4)],
    '04/01/2023': [("Study", 5), ("Bike", 15), ("Sleep", 4)],
}
"""
from data.data import activities

new_activities = {}

for day in activities:
    date = day.split('\n')[1]
    new_activities[date] = activities[day]

print(new_activities)

