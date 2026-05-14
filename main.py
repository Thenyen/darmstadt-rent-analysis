from data.scraper import generate_sample_data
from data.clean import clean_data, summarize_by_district
from data.map import create_heatmap

df = generate_sample_data()
df = clean_data(df)
summary = summarize_by_district(df)

m = create_heatmap(summary)
m.save("map.html")
print("Map saved to map.html")