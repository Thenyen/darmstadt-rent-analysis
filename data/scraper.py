import pandas as pd
import random

DISTRICTS = [
    "Darmstadt-Mitte",
    "Darmstadt-Nord",
    "Darmstadt-Ost",
    "Darmstadt-West",
    "Darmstadt-Bessungen",
    "Darmstadt-Eberstadt",
    "Darmstadt-Arheiligen",
    "Darmstadt-Kranichstein",
    "Darmstadt-Wixhausen"
]

random.seed(42)

def generate_sample_data(n=300):
    rows = []
    for _ in range(n):
        district = random.choice(DISTRICTS)
        size = random.randint(30, 120)

        base_price = {
            "Darmstadt-Mitte": 16.0,
            "Darmstadt-Nord": 13.5,
            "Darmstadt-Ost": 14.5,
            "Darmstadt-West": 14.5,
            "Darmstadt-Bessungen": 14.0,
            "Darmstadt-Eberstadt": 12.5,
            "Darmstadt-Arheiligen": 12.0,
            "Darmstadt-Kranichstein": 11.0,
            "Darmstadt-Wixhausen": 10.5
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