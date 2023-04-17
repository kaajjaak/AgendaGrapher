from data.data import activities, screen_activities
from graphers.bar_grapher import create_bar_chart

create_bar_chart(activities, screen_activities, 'Total Screentime')
