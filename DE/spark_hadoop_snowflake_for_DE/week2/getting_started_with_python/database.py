from DE.spark_hadoop_snowflake_for_DE.week2.python_examples.utils import get_conn


conn = get_conn()

"""
    The next step is to create a database. Databases contain your schemas, which contain your database objects. 
    We can create one in a similar manner to creating a warehouse, but this time with the CREATE DATABASE command.
"""
# conn.cursor().execute("CREATE DATABASE IF NOT EXISTS testdb")

"""
    Again, creating a database also sets that database as the active one for the current session. 
    If you need to set an already created database as the active database for the session, use the USE DATABASE command.
"""

# conn.cursor().execute("USE DATABASE testdb")
