import pandas as pd

file_name = "LinkFire.csv"
df = pd.read_csv(file_name)

#How many total pageview events did the links in the provided dataset receive in the full period?
# How many per day?
pageview_data = df[df['event'] == 'pageview']
total_pageviews = len(pageview_data)

daily_pageviews = pageview_data.groupby('date').size()

print(f"Total pageview events: {total_pageviews}")
print("Pageview events per day:")
print(daily_pageviews)