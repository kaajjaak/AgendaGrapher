def calculate_total_amount(activities, counted_activities):
    total_times = []
    for day, tmp_activities in activities.items():
        # count how many times
        total_times.append(len([activity for activity, duration in tmp_activities if activity in counted_activities]))
    return total_times
