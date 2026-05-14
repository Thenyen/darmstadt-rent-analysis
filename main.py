from data.scraper import generate_sample_data
from data.clean import clean_data, summarize_by_district

df = generate_sample_data()
df = clean_data(df)
summary = summarize_by_district(df)

print(summary)