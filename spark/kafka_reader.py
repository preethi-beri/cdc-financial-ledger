from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Kafka CDC Reader")
    .master("local[*]")
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.13:4.0.1"
    )
    .getOrCreate()
)

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "fintech.public.transactions")
    .option("startingOffsets", "earliest")
    .load()
)

query = (
    df.selectExpr("CAST(value AS STRING)")
    .writeStream
    .format("console")
    .outputMode("append")
    .start()
)

query.awaitTermination()