#!/usr/bin/env python
import snowflake.connector
import os
from dotenv import load_dotenv


def get_conn():
    # Load environment variables from .env
    load_dotenv()

    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        session_parameters={
            'QUERY_TAG': 'EndOfMonthFinancials',
        }
    )
    return conn
