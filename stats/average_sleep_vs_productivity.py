from stats.average_productivity import get_average_productivity

def get_average_sleep(activities, productive_activities):
    average_productivity = get_average_productivity(activities, productive_activities)
    sleep_amounts = []
    for day, activities in activities.items():
        day_productivity = 0
        for activity in activities:
            if activity[0] in productive_activities:
                day_productivity += activity[1]
        if day_productivity >= average_productivity:
            sleep_amount = 0
            for activity in activities:
                if activity[0] == "Sleep":
                    sleep_amount += activity[1]
            sleep_amounts.append(sleep_amount)
    return sum(sleep_amounts)/len(sleep_amounts)


