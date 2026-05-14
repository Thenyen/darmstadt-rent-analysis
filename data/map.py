import folium
import pandas as pd

def create_heatmap(summary: pd.DataFrame):
    m = folium.Map(location=[49.8728, 8.6512], zoom_start=12)

    folium.Choropleth(
        geo_data="data/stadtteile_wgs84.geojson",
        data=summary,
        columns=["district", "avg_price_per_sqm"],
        key_on="feature.properties.DAStadttei",
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=0.5,
        legend_name="Avg. Price per sqm (€)",
        nan_fill_color="lightgray"
    ).add_to(m)

    folium.LayerControl().add_to(m)

    return m