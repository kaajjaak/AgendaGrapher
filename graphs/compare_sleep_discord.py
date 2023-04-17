from data.data import activities
from graphers.comparison_grapher import comparison_graph

group_one = ["Discord"]
group_two = ["Sleep"]
group_one_color = "lightgray"
group_two_color = "lightpink"
group_one_name = "Discord"
group_two_name = "Sleep"

comparison_graph(activities, group_one, group_two, group_one_color, group_two_color, group_one_name, group_two_name,
                 line_color="darkblue")
