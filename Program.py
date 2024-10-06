import pandas as pd

file_name = "LinkFire.csv"
df = pd.read_csv(file_name)

# How many total pageview events did the links in the provided dataset receive in the full period?
# How many per day?
pageview_data = df[df['event'] == 'pageview']
total_pageviews = len(pageview_data)

daily_pageviews = pageview_data.groupby('date').size()

print(f"Total pageview events: {total_pageviews}")
print("Pageview events per day:")
print(daily_pageviews)
print("\n")

# What about the other recorded events?
other_events_data = df[df['event'] != 'pageview']
other_events_data_by_type = other_events_data['event'].value_counts()

daily_other_events = other_events_data.groupby(['date', 'event']).size()

print("Other events:")
print(other_events_data_by_type)
print("Other events per day: ")
print(daily_other_events)
print("\n")

