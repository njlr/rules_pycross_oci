import pytest
from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as F

def uppercase_column(df: DataFrame, col_name: str) -> DataFrame:
    """Converts the specified string column to uppercase."""
    return df.withColumn(col_name, F.upper(F.col(col_name)))

@pytest.fixture(scope="session")
def spark():
    """Fixture to initialize a local Spark Session for testing."""
    spark_session = (
        SparkSession.builder
        .master("local[1]")  # Run locally with a single thread
        .appName("pyspark-unit-tests")
        .getOrCreate()
    )
    yield spark_session
    spark_session.stop()

def test_uppercase_column(spark):
    input_data = [("alice",), ("bob",)]
    input_df = spark.createDataFrame(input_data, ["name"])

    actual_df = uppercase_column(input_df, "name")
    actual_data = sorted([tuple(row) for row in actual_df.collect()])

    expected_data = sorted([("ALICE",), ("BOB",)])

    assert actual_data == expected_data
