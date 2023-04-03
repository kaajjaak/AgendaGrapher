from util.main_grapher import create_graph
from data.data import activities, activity_groups_colors, activity_groups
from util.grouper import map_activities


print(map_activities(activities, activity_groups))
create_graph(map_activities(activities, activity_groups), activity_groups_colors)