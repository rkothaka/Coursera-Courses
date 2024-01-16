# https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-pandas

"""
Reading data from a Snowflake database to a pandas DataFrame
To read data into a pandas DataFrame,
you use a Cursor to retrieve the data and then call one of these Cursor methods
to put the data into a pandas DataFrame:

fetch_pandas_all().
fetch_pandas_batches().


Writing data from a pandas DataFrame to a Snowflake database
To write data from a pandas DataFrame to a Snowflake database, do one of the following:

Call the write_pandas() function.

Call the pandas.DataFrame.to_sql() method (see the pandas documentation),
and specify pd_writer() as the method to use to insert the data into the database.
"""

import pandas as pd
from utils import connection


def fetch_pandas_old(cur, sql: str) -> pd.DataFrame:
    cur.execute(sql)
    rows = 0
    while True:
        dat = cur.fetchmany(50000)
        if not dat:
            break
        df = pd.DataFrame(dat, columns=[d[0] for d in cur.description])
        rows += df.shape[0]
    print(rows)
    return df


cur = connection.get_conn().cursor()
cur.execute("USE SCHEMA DEV.CDM")
sql = "SELECT * FROM test_table"
test_table_df = fetch_pandas_old(cur, sql)

print(test_table_df)
