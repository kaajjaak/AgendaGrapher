from data.data import activities, productive_activities
from stats.average_sleep_vs_productivity import get_average_sleep

print("Average hours of sleep on more than average productive day:", round(get_average_sleep(activities, productive_activities), 2))