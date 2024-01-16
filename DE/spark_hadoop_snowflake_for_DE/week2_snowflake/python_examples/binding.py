# https://docs.snowflake.com/developer-guide/python-connector/python-connector-example?_fsi=P9kkfr0A#binding-data

from utils import connection


conn = connection.get_conn()

conn.cursor().execute("USE SCHEMA DEV.CDM")

conn.cursor().execute(
    "CREATE OR REPLACE TABLE "
    "test_table(col1 integer, col2 string)")


"""
To specify values to be used in a SQL statement, you can include literals in the statement, or you can bind variables. 
When you bind variables, you put one or more placeholders in the text of the SQL statement, 
and then specify the variable (the value to be used) for each placeholder.
"""

# Literal
conn.cursor().execute(
    "INSERT INTO test_table(col1, col2) VALUES " +
    "    (123, 'test string1'), " +
    "    (456, 'test string2')")

# Binding
conn.cursor().execute(
    "INSERT INTO test_table(col1, col2) "
    "VALUES(%s, %s)", (
        789,
        'test string3'
    ))


"""
    Both pyformat binding and format binding bind data on the client side rather than on the server side.

    By default, the Snowflake Connector for Python supports both pyformat and format, 
    so you can use %(name)s or %s as the placeholder. For example:
"""
conn.cursor().execute(
    "INSERT INTO test_table(col1, col2) "
    "VALUES(%(col1)s, %(col2)s)", {
        'col1': 800,
        'col2': 'test string4',
        })


# Binding data for IN operator
rec1, rec2 = conn.cursor().execute(
    "SELECT col1, col2 FROM test_table"
    " WHERE col2 IN (%s)", (
        ['test string1', 'test string3'],
    ))
print("test_table contents where col2 contains 'test_string1' or 'test_string3'")
print('{0}, {1}'.format(rec1, rec2))

conn.close()

# Binding parameters to variables for batch inserts
import snowflake.connector
snowflake.connector.paramstyle='qmark'

conn = connection.get_conn()
conn.cursor().execute("USE SCHEMA DEV.CDM")

rows_to_insert = [(101, 'milk'), (102, 'apple'), (103, 'egg')]

conn.cursor().executemany(
    "insert into test_table (col1, col2) values (?, ?)",
    rows_to_insert)

conn.close()