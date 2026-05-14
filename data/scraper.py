import pandas as pd
import random

DISTRICTS = [
    "Mitte", "Eberstadt", "Bessungen", "Kranichstein",
    "Arheilgen", "Wixhausen", "Darmstadt-Nord", "Martinsviertel",
    "Johannesviertel", "Oststadt", "Weststadt", "Paulusviertel"
]

random.seed(42)

def generate_sample_data(n=300):
    rows = []
    for _ in range(n):
        district = random.choice(DISTRICTS)
        size = random.randint(30, 120)

        base_price = {
            "Mitte": 16, "Martinsviertel": 15.5, "Paulusviertel": 15,
            "Oststadt": 14.5, "Weststadt": 14.5, "Bessungen": 14,
            "Johannesviertel": 13.5, "Darmstadt-Nord": 13,
            "Arheilgen": 12, "Eberstadt": 12.5,
            "Kranichstein": 11, "Wixhausen": 10.5
        }

        price_per_sqm = round(base_price[district] + random.uniform(-1.5, 1.5), 2)
        total_rent = round(price_per_sqm * size, 2)

        rows.append({
            "district": district,
            "size_sqm": size,
            "price_per_sqm": price_per_sqm,
            "total_rent": total_rent
        })

    return pd.DataFrame(rows)