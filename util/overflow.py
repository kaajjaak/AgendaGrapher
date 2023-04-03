from data.data import activities


def adjust_activities(input_dict):
    activities = input_dict.copy()
    for day, acts in activities.items():
        total_hours = sum([x[1] for x in acts])
        deviation_hours = round(24 - total_hours, 3)
        if abs(deviation_hours) >= 0.001:
            if deviation_hours > 0:
                acts[-1] = (acts[-1][0], round(acts[-1][1] + deviation_hours, 3))
                print(
                    f"On {day}, {deviation_hours} hours need to be removed from {acts[-2][0]} and added to {acts[-1][0]}.")
            else:
                acts[-1] = (acts[-1][0], round(acts[-1][1] + deviation_hours, 3))
                print(
                    f"On {day}, {abs(deviation_hours)} hours need to be removed from {acts[-1][0]} and added to {acts[-2][0]}.")
    return {day: [(act[0], round(act[1], 3)) for act in acts] for day, acts in activities.items()}


print(adjust_activities(activities))
