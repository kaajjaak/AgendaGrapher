def get_average_productivity(activities, productive_activities):
    group_one_totals = []
    group_one = productive_activities
    for day, activities in activities.items():
        group_one_total = 0
        group_two_total = 0
        for activity in activities:
            if activity[0] in group_one:
                group_one_total += activity[1]
        group_one_totals.append(group_one_total)
    return sum(group_one_totals)/len(group_one_totals)