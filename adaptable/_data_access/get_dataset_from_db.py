import psycopg2
import pandas as pd
import pkg_resources


def select_table(conn, query_file, variables) -> pd.DataFrame:
    sql_path = pkg_resources.resource_filename(__name__, query_file)

    with open(sql_path, "r") as r_file:
        query = r_file.read()
    try:
        sql_query = pd.read_sql_query(sql=query, params=variables, con=conn)
    except Exception as e:
        print(e)
    df = pd.DataFrame(sql_query)
    return df


def alter_table(conn, query_file, variables_as_tuple):
    sql_path = pkg_resources.resource_filename(__name__, query_file)
    updated_rows = 0
    try:
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE statement
        with open(sql_path, "r") as r_file:
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
