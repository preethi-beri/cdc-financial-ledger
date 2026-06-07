from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("CDC Financial Ledger")
    .master("local[*]")
    .getOrCreate()
)

print("=" * 50)
print("SPARK STARTED SUCCESSFULLY")
print("=" * 50)

spark.stop()