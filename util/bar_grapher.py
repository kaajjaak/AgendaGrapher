import matplotlib.pyplot as plt
from util.count_hours import calculate_total_hours


def create_bar_chart(activities, counted_activities, title="Total Screentime"):
    # Create list of total hours for each day
    total_hours = calculate_total_hours(activities, counted_activities)

    # Create bar chart for total hours
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(list(activities.keys()), total_hours, color='blue')
    plt.xticks(rotation=45, ha="right", fontsize=7)

    # Calculate the maximum value of the data
    max_value = max(total_hours)

    # Calculate the range of values for the horizontal lines
    start = 2.5
    end = max_value + 2.5
    step = 2.5

    number_of_lines = int((end - start) // step)

    for i in range(number_of_lines):
        value = start + i * step
        ax.axhline(value, color='gray', alpha=0.5, linestyle='--')

    # Add labels and formatting
    ax.set_ylabel('Total hours')
    ax.set_xlabel('Day')
    ax.set_title(title)

    plt.show()
