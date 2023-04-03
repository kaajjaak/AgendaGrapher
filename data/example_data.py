def convert_to_hours(minutes, hours=0):
    return hours + minutes / 60


activities = {
    'Monday': [("Breakfast", 1), ("Gaming", 22), ("Sleep", 1)],
    'Tuesday': [("Study", 19), ("Lunch", 1), ("Sleep", 4)],
}

activity_colors = {
    'Breakfast': '#FFD700',
    'Gaming': '#FF0000',
    'Sleep': '#000000',
    'Study': '#0000FF',
    'Lunch': '#FFD700',
}

activity_groups = {
    'Eating': ['Breakfast', 'Lunch'],
    'Sleeping': ['Sleep'],
    'Studying': ['Study'],
    'Gaming': ['Gaming'],
}

activity_groups_colors = {
    'Eating': '#FFD700',
    'Sleeping': '#000000',
    'Studying': '#0000FF',
    'Gaming': '#FF0000',
}

productive_activities = ['Study']