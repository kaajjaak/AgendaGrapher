def calculate_total_hours(activities, counted_activities):
    total_hours = []
    for day, tmp_activities in activities.items():
        total_day_hours = sum(duration for activity, duration in tmp_activities if activity in counted_activities)
        total_hours.append(total_day_hours)
    return total_hours
