# take the acivity dictionary and convert it to a new dictionary with the activity groups as keys
def map_activities(input_dict, activity_groups):
    output_dict = {}
    for day, activities in input_dict.items():
        mapped_activities = []
        for activity, duration in activities:
            group_found = False
            for group, group_activities in activity_groups.items():
                if activity in group_activities:
                    mapped_activities.append((group, duration))
                    group_found = True
                    break
            if not group_found:
                mapped_activities.append((activity, duration))
        output_dict[day] = mapped_activities
    return output_dict