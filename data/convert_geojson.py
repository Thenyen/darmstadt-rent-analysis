import json
from pyproj import Transformer

transformer = Transformer.from_crs("EPSG:25832", "EPSG:4326", always_xy=True)

with open("data/stadtteile.geojson", "r") as f:
    geojson = json.load(f)

def convert_coords(coords):
    if isinstance(coords[0], list):
        return [convert_coords(c) for c in coords]
    lon, lat = transformer.transform(coords[0], coords[1])
    return [lon, lat]

for feature in geojson["features"]:
    geom = feature["geometry"]
    geom["coordinates"] = convert_coords(geom["coordinates"])

with open("data/stadtteile_wgs84.geojson", "w") as f:
    json.dump(geojson, f)

print("Done — saved to data/stadtteile_wgs84.geojson")
