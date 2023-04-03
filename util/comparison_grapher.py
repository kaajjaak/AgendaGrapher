import matplotlib.pyplot as plt


def comparison_graph(activities_dict, group_one, group_two, group_one_color, group_two_color, group_one_name, group_two_name ,line_color="darkorange"):
    group_one_totals = []
    group_two_totals = []
    group_ratios = []

    for day, activities in activities_dict.items():
        group_one_total = 0
        group_two_total = 0
        for activity in activities:
            if activity[0] in group_one:
                group_one_total += activity[1]
            elif activity[0] in group_two:
                group_two_total += activity[1]
        group_one_totals.append(group_one_total)
        group_two_totals.append(group_two_total)
        group_ratios.append(group_one_total / group_two_total if group_two_total > 0 else 0)

    bar_width = 0.4  # Width of the bars

    # Set the figure size to adjust the height
    plt.figure(figsize=(9, 6.5))

    plt.bar([i - bar_width / 2 for i in range(len(activities_dict))], group_one_totals, width=bar_width,
            color=group_one_color, label=group_one_name)
    plt.bar([i + bar_width / 2 for i in range(len(activities_dict))], group_two_totals, width=bar_width,
            color=group_two_color, label=group_two_name)
    plt.legend(loc="upper left", labels=[group_one_name, group_two_name])

    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.xticks(range(len(activities_dict)), activities_dict.keys())
    plt.ylabel("Time (hours)")

    ax1 = plt.gca() # get current axes instance
    ax1.set_ylim(bottom=0, top=max(group_one_totals + group_two_totals) + 2) # set y limit

    ax2 = ax1.twinx() # create second y-axis instance
    ax2.plot(group_ratios, color=line_color, marker="o", markersize=4, label="Ratio")
    ax2.set_ylim(bottom=0)

    for i in range(2, 14, 2):
        ax1.axhline(i, color='gray', alpha=0.5, linestyle='--') # add horizontal lines to the first y-axis

    plt.legend(loc="upper right")

    for i, ratio in enumerate(group_ratios):
        if ratio < ax2.get_ylim()[1]:
            ax2.text(i, ratio + 0.1, f"{ratio:.1f}", ha="center", fontsize=8)

    plt.show()
