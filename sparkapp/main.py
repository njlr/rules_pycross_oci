from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main() -> None:
  spark = (
    SparkSession.builder
    .appName("PySpark Sales Demo")
    .master("local[*]")
    .getOrCreate()
  )

  sales = [
    ("London", "Books", 2, 15.00),
    ("London", "Electronics", 1, 250.00),
    ("Manchester", "Books", 3, 12.00),
    ("Manchester", "Electronics", 2, 180.00),
    ("Edinburgh", "Books", 4, 10.00),
    ("Edinburgh", "Furniture", 1, 300.00),
  ]

  dataframe = spark.createDataFrame(
    sales,
    schema=["city", "category", "quantity", "unit_price"],
  )

  revenue_by_category = (
    dataframe
    .withColumn(
      "revenue",
      F.col("quantity") * F.col("unit_price"),
    )
    .groupBy("category")
    .agg(
      F.sum("quantity").alias("items_sold"),
      F.round(F.sum("revenue"), 2).alias("total_revenue"),
    )
    .orderBy(F.desc("total_revenue"))
  )

  print("Source sales")
  dataframe.show(truncate=False)

  print("Revenue by category")
  revenue_by_category.show(truncate=False)

  revenue_by_category.write.mode("overwrite").parquet(
    "output/revenue-by-category",
  )

  spark.stop()


if __name__ == "__main__":
  main()