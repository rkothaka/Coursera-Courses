from DE.spark_hadoop_snowflake_for_DE.week2.python_examples.utils import get_conn


con = get_conn()

"""
    The CREATE WAREHOUSE command creates a warehouse, as expected, 
    but also implicitly sets that warehouse as the active warehouse for your session. 
    If you've already created a warehouse, 
    you can explicitly set it as the active warehouse with the USE WAREHOUSE command.
"""

# conn.cursor().execute("CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg")

# conn.cursor().execute("USE WAREHOUSE tiny_warehouse_mg")

