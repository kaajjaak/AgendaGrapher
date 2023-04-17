import matplotlib.pyplot as plt

from util.count_amount import calculate_total_amount
from util.count_hours import calculate_total_hours


def create_line_graph(activities, counted_activities, graph_name="Productivity Chart", measure='value'):
    if measure == 'value':
        total_hours = calculate_total_hours(activities, counted_activities)
    elif measure == 'amount':
        total_hours = calculate_total_amount(activities, counted_activities)
    # Create list of total productive hours for each day
    total_hours = calculate_total_hours(activities, counted_activities)

    # Create line chart for productive hours
    # make the labels at the bottom smaller
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(list(activities.keys()), total_hours, color='orange')
    plt.xticks(rotation=45, ha="right", fontsize=7)

    # Calculate the range of values for the horizontal lines
    start = 2
    end = max(total_hours) + 2
    step = 2

    number_of_lines = int((end - start) // step)

    for i in range(number_of_lines):
        value = start + i * step
        ax.axhline(value, color='gray', alpha=0.5, linestyle='--')
    # Add labels and formatting
    if measure == 'value':
        ax.set_ylabel('Total hours')
    elif measure == 'count':
        ax.set_ylabel('Total amount')
    ax.set_xlabel('Day')
    ax.set_title(graph_name)

    plt.show()
