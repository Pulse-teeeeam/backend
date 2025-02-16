import json
import random
from shapely.geometry import shape, Point

with open("9.geojson", encoding="utf-8") as f:
    data = json.load(f)


def random_point(point: str):
    tulgansky_district = None
    for feature in data["features"]:
        if feature["properties"].get("name") == point:
            tulgansky_district = shape(feature["geometry"])
            break

    if tulgansky_district is None:
        return 'POINT (6207807.732771615 6840847.728369174)'
    else:
        def random_point_in_polygon(polygon):
            minx, miny, maxx, maxy = polygon.bounds
            while True:
                p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
                if polygon.contains(p):
                    return p

        random_point = random_point_in_polygon(tulgansky_district)
        return random_point
