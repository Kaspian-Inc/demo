from h3 import h3
from pyspark.sql.functions import col, lit, udf


@udf
def get_h3_10(lat: float, lon: float) -> str:
    return h3.geo_to_h3(float(lat), float(lon), 10)


def main(input_data: dict):
    df_starbucks = input_data["starbucks"]
    df_starbucks = df_starbucks.withColumn(
        "h3_10", get_h3_10(col("lat"), col("lon"))
    )
    return df_starbucks
