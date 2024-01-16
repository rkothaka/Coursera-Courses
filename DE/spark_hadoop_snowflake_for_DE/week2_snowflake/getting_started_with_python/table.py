from utils import connection


conn = connection.get_conn()

conn.cursor().execute("USE SCHEMA DEV.CDM")


"""
    Alright, with a warehouse, database, 
    and schema created you have everything you need to begin manipulating data in tables. 
    First, you'll need to create the table. That's done with the CREATE TABLE command.
"""
# conn.cursor().execute(
#     "CREATE OR REPLACE DEMO_1 "
#     "test_table(NAME string)")


"""
    With the table test_table created, you can add data to it. You can do so with the command INSERT.
"""
conn.cursor().execute(
    "INSERT INTO DEMO_1(NAME) "
    "VALUES('test string1'),('test string2')")


"""
    If you don't want to manually insert data row by row, however, you can load data instead. 
    This is done with a combination of the PUT and COPY INTO commands.
"""
# conn.cursor().execute("PUT file:///tmp/data/file* @%DEMO_1")
# conn.cursor().execute("COPY INTO DEMO_1")

"""
    The PUT command here is staging the file, 
    and the COPY INTO command is copying that data from that file into the specified table. 
    You can also use the COPY INTO command to copy data from an external location.
"""


# Query Data
"""
    Of course, you'll want to query your data at some point. 
    It's easy to do that within the Python Connector too. 
    To view values from the table, you can do so easily with the print command.
"""
col1 = conn.cursor().execute("SELECT NAME col2 FROM DEMO_1").fetchall()
print('{0}'.format(col1))

conn.close()
