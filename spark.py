from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("MinIO Data Processing") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "ROOTUSER") \
    .config("spark.hadoop.fs.s3a.secret.key", "CHANGEME123") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()
