from data.data import activities, productive_activities
import matplotlib.pyplot as plt

# Create list of total productive hours for each day
productive_hours = []
for day, tmp_activities in activities.items():
    total_productive_hours = sum(duration for activity, duration in tmp_activities if activity in productive_activities)
    productive_hours.append(total_productive_hours)

# Create line chart for productive hours
# make the labels at the bottom smaller
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(list(activities.keys()), productive_hours, color='orange')
plt.xticks(rotation=45, ha="right", fontsize=7)

for i in range(2, 14, 2):
    ax.axhline(i, color='gray', alpha=0.5, linestyle='--')
# Add labels and formatting
ax.set_ylabel('Total productive hours')
ax.set_xlabel('Day')
ax.set_title('Productivity Chart')

plt.show()
