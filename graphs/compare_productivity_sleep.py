from data.data import activities, productive_activities
from graphers.line_comparison_grapher import create_line_graph

sleep = ["Sleep"]

create_line_graph(activities, productive_activities, sleep, "Productivity", "Sleep", "Productivity VS Sleep Chart")
