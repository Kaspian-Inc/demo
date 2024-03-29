# Aggregate Citibike Trips

from math import radians, cos, sin, asin, sqrt

# From https://stackoverflow.com/questions/15736995/how-can-i-quickly-estimate-the-distance-between-two-latitude-longitude-points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r

def main(input_data, metadata):

    # Extract dataframe
    df_citibikes = input_data["df_citibikes"]

    # Compute trip distance
    df_citibikes["distance"] = df_citibikes.apply(
        lambda row: haversine(
            row["start_lon"],
            row["start_lat"],
            row["end_lon"],
            row["end_lat"],
        ), axis=1
    )

    # Aggregate
    df_citibikes = df_citibikes.drop(["start_lat", "start_lon"], axis=1)
    df_citibikes = df_citibikes.groupby(["end_lat", "end_lon"]).mean().reset_index()

    # Reformat and return
    df_citibikes = df_citibikes.rename(
        columns={
            "end_lat": "lat",
            "end_lon": "lon",
            "duration": "avg_duration",
            "distance": "avg_distance"
        }
    )
    return {
        'data': {'citibikes': df_citibikes},
        'metadata': metadata,
    }
  
