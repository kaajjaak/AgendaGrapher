from datetime import datetime


def get_activities_from_start_date(activities, start_date):
    start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
    result = {}
    for date_str in activities.keys():
        date = datetime.strptime(date_str, '%d/%m/%Y').date()
        if date >= start_date:
            result[date_str] = activities[date_str]
    return result
