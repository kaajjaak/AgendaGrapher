import matplotlib.pyplot as plt
from data.data import activities
from util.comparison_grapher import comparison_graph

group_one = ["Sleep"]
group_two = ["Discord", "Junk YouTube"]
group_one_color = "lightpink"
group_two_color = "lightblue"
group_one_name = "Sleep"
group_two_name = "Social Media"

comparison_graph(activities, group_one, group_two, group_one_color, group_two_color, group_one_name, group_two_name,
                 line_color="darkblue")
