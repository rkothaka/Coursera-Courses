from DE.spark_hadoop_snowflake_for_DE.week2_snowflake.python_examples.utils import  get_conn


conn = get_conn()


"""
    Schemas are the grouping of your database objects. 
    These include your tables, the data within them, and views. 
    Schemas are found within databases. 
    You can create a schema with the CREATE SCHEMA command.
"""
# conn.cursor().execute("CREATE SCHEMA IF NOT EXISTS testschema")

"""
    Since CREATE SCHEMA also sets it as the active schema for your session, 
    you don't have to explicitly call USE SCHEMA as well. 
    Only do so if you would like to use an already created schema.
"""
# conn.cursor().execute("USE SCHEMA testschema")

"""
    By default, the schema will be used in the current database. 
    You can use it in another database by specifying that other database.
"""
# conn.cursor().execute("USE SCHEMA otherdb.testschema")
