import psycopg2
import pandas as pd


def select_table(conn, query_file, variables) -> pd.DataFrame:
    with open(query_file, "r") as r_file:
        query = r_file.read()
    try:
        sql_query = pd.read_sql_query(sql=query, params=variables, con=conn)
    except Exception as e:
        print(e)
    df = pd.DataFrame(sql_query)
    return df


def alter_table(conn, query_file, variables_as_tuple):
    updated_rows = 0
    try:
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE statement
        with open(query_file, "r") as r_file:
            query = r_file.read()
        cur.execute(query, variables_as_tuple)
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Command adapted for PostgreSQL databases to close the communication
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return updated_rows
