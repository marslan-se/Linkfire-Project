import pandas as pd

file_name = "LinkFire.csv"
df = pd.read_csv(file_name)

# How many total pageview events did the links in the provided dataset receive in the full period?
# How many per day?
pageview_data = df[df['event'] == 'pageview']
total_pageviews = len(pageview_data)

daily_pageviews = pageview_data.groupby('date').size()

print(f"Total pageview events: {total_pageviews}")
print("\n")
print("Pageview events per day:")
print(daily_pageviews)
print("\n")

# What about the other recorded events?
other_events_data = df[df['event'] != 'pageview']
other_events_data_by_type = other_events_data['event'].value_counts()

daily_other_events = other_events_data.groupby(['date', 'event']).size()

print("Other events:")
print(other_events_data_by_type)
print("\n")
print("Other events per day: ")
print(daily_other_events)
print("\n")

# Which countries did the pageviews come from?
pageview_countires = pageview_data['country'].value_counts()

print("Pageviews by country:")
print(pageview_countires)
print("\n")

# What was the overall click rate (clicks/pageviews)?
click_event_data = df[df['event'] == 'click']
total_clicks = len(click_event_data)

if total_pageviews > 0:
    click_rate = total_clicks / total_pageviews
else:
    click_rate = 0

print(f"Total pageviews: {total_pageviews}")
print(f"Total clicks: {total_clicks}")
print(f"Overall click rate (clicks/pageviews): {click_rate:.4f}")
print("\n")

# How does the clickrate distribute across different links?
link_data = df.groupby('linkid').agg({'event': 'count'}).reset_index()
link_data.rename(columns={'event': 'clicks'}, inplace=True)

link_data['pageviews'] = link_data['clicks']  # Assuming each click is a pageview

link_data['click_rate'] = link_data['clicks'] / link_data['pageviews']
link_data['click_rate'] = link_data['click_rate'].fillna(0)

print("Click rate distribution across different links:")
print(link_data[['linkid', 'clicks', 'pageviews', 'click_rate']])