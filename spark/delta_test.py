from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

builder = (
    SparkSession.builder
    .appName("Delta Lake Test")
    .master("local[*]")
    .config(
        "spark.sql.extensions",
        "io.delta.sql.DeltaSparkSessionExtension"
    )
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog"
    )
)

spark = configure_spark_with_delta_pip(builder).getOrCreate()

data = [
    (1, 101, 5000),
    (2, 102, 7000),
    (3, 103, 12000)
]

df = spark.createDataFrame(
    data,
    ["transaction_id", "user_id", "amount"]
)

df.write.format("delta").mode("overwrite").save(
    "delta-lake/transactions"
)

print("Delta table created successfully!")

spark.stop()