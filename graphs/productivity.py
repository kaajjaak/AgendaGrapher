from data.data import activities, productive_activities
from graphers.line_grapher import create_line_graph

create_line_graph(activities, productive_activities, "Productivity Chart")
