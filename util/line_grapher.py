import matplotlib.pyplot as plt


def line_graph(activities, counted_activities, graph_name="Productivity Chart"):
    # Create list of total productive hours for each day
    hours = []
    for day, tmp_activities in activities.items():
        total_hours = sum(
            duration for activity, duration in tmp_activities if activity in counted_activities)
        hours.append(total_hours)

    # Create line chart for productive hours
    # make the labels at the bottom smaller
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(list(activities.keys()), hours, color='orange')
    plt.xticks(rotation=45, ha="right", fontsize=7)

    for i in range(2, 14, 2):
        ax.axhline(i, color='gray', alpha=0.5, linestyle='--')
    # Add labels and formatting
    ax.set_ylabel('Total hours')
    ax.set_xlabel('Day')
    ax.set_title(graph_name)

    plt.show()
