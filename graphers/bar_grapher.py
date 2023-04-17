import matplotlib.pyplot as plt

from util.count_amount import calculate_total_amount
from util.count_hours import calculate_total_hours
import numpy as np


def create_bar_chart(activities, counted_activities, title="Total Screentime", measure='value'):
    if measure == 'value':
        total_hours = calculate_total_hours(activities, counted_activities)
    elif measure == 'amount':
        total_hours = calculate_total_amount(activities, counted_activities)

    # Calculate the average total hours
    avg_total_hours = np.mean(total_hours)

    # Create bar chart for total hours
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(list(activities.keys()), total_hours, color='blue')
    plt.xticks(rotation=45, ha="right", fontsize=7)

    # Calculate the maximum value of the data
    max_value = max(total_hours)

    # Calculate the range of values for the horizontal lines
    start = 1
    end = max_value + 1
    step = 1

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
    ax.set_title(title)

    # Add average to legend
    ax.legend([f'Average: {avg_total_hours:.0f}'])

    plt.show()
