import airflow
from importlib.metadata import version

print("Hello, world!")
print(f"Imported: {airflow.__name__}")
print(f"Version: {version('apache-airflow')}")