from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("MongoDB Integration") \
    .config("spark.mongodb.input.uri", "mongodb://localhost:27017/music_database.audio_features") \
    .config("spark.mongodb.output.uri", "mongodb://localhost:27017/music_database.audio_features") \
    .getOrCreate()

# Load data from MongoDB into a DataFrame
dataFrame = spark.read.format("mongo") \
    .load()

# Show the DataFrame schema
dataFrame.printSchema()

# Show the first few rows of the DataFrame
dataFrame.show()

