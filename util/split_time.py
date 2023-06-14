def convert_hours_to_hours_and_minutes(hours):
    return int(hours), int((hours - int(hours)) * 60)
