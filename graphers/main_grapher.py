import matplotlib.pyplot as plt
import numpy as np

# Define the weekly routine as a dictionary of lists of (activity, duration) tuples


def create_graph(activities, activity_color):
    # Create a stacked horizontal bar chart for the entire week
    fig, ax = plt.subplots(figsize=(14, 12))
    for i, (day, activities) in enumerate(activities.items()):
        durations = [activity[1] for activity in activities]
        left = np.zeros(len(durations))
        for j, duration in enumerate(durations):
            activity, _ = activities[j]
            ax.barh(day, duration, left=left, color=activity_color[activity], label=activity if j == 0 else None,
                    height=0.8)
            left += duration

    # Add labels and formatting
    ax.set_ylabel('Day of the week')
    ax.set_xlabel('Time')
    ax.set_title('Akina\'s Activities Graph')
    ax.invert_yaxis()

    # Create a single legend entry for each activity
    handles, labels = [], []
    for activity, color in activity_color.items():
        if activity == 'DST':
            continue
        handles.append(plt.Rectangle((0, 0), 1, 1, color=color))
        labels.append(activity)
    ax.legend(handles, labels, loc='upper left', bbox_to_anchor=(1.0, 1.0))

    # Set the x-ticks and labels
    ax.set_xticks(np.arange(0, 25))
    ax.set_xticklabels([f'{i}:00' for i in range(24)] + ['24:00'], rotation=45, ha='right')

    # Add vertical lines for each hour
    for i in range(25):
        ax.axvline(i, color='gray', alpha=0.5, linestyle='--')

    plt.tight_layout()
    plt.show()
