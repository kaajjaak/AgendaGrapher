from data.data import activities, productive_activities
from stats.average_sleep_vs_productivity import get_average_sleep_to_productivity
from stats.average import get_average
from util.split_time import convert_hours_to_hours_and_minutes

hours, minutes = convert_hours_to_hours_and_minutes(get_average_sleep_to_productivity(activities, productive_activities))
print("Average hours of sleep on more than average productive day: {} hours and {} minutes".format(hours, minutes))

hours, minutes = convert_hours_to_hours_and_minutes(get_average(activities, ["Sleep"]))
print("General average amount of hours of sleep: {} hours and {} minutes".format(hours, minutes))