import pandas as pd

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Remove rows with missing values
    df = df.dropna()

    # Remove unrealistic values
    df = df[df["price_per_sqm"] > 5]
    df = df[df["price_per_sqm"] < 30]
    df = df[df["size_sqm"] > 10]
    df = df[df["size_sqm"] < 300]

    # Round price columns
    df["price_per_sqm"] = df["price_per_sqm"].round(2)
    df["total_rent"] = df["total_rent"].round(2)

    return df

def summarize_by_district(df):
    summary = df.groupby("district").agg(
        avg_price_per_sqm=("price_per_sqm", "mean"),
        avg_total_rent=("total_rent", "mean"),
        avg_size=("size_sqm", "mean"),
        count=("district", "count")
    ).round(2).reset_index()

    return summary