from data.data import activities
from graphers.bar_grapher import create_bar_chart
from util.splice_data import get_activities_from_start_date

create_bar_chart(get_activities_from_start_date(activities, '05/04/2023'), ["Eating"], 'Total Meal Count', 'amount')
