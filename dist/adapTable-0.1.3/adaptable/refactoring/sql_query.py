from adaptable.refactoring._utils import (
    retrieve_the_metabase_cards_using_sql_query_with_a_table,
    update_report_card_with_new_column,
)


def renaming_sql_query_column(
    conn, old_column_name: str, new_column_name: str, table_name: str, schema_name: str
):
    """Renaming a column in all the sql query created. WARNING : could have side effect, depending on SQL standard used
    across all your Metabase.

    Parameters
    ----------
    conn: psycopg2 DBAPI2 connector
        Connexion to your Metabase Database
    old_column_name : str
        Former name of the column
    new_column_name : str
        New name of the column
    table_name : str
        Table name that contains this column
    schema_name : str
        Schema name that contains the column table

    Returns
    -------
    Nothing as it has been build to change the Metabase DB synchronously.
    """
    # Try to fix the sql query

    print("Warning: Working on sql query")
    # Step 1 : find all the query concerned by searching for native query_type and IN contain
    # old column with right schema and tables
    df_metabase_cards = retrieve_the_metabase_cards_using_sql_query_with_a_table(
        conn=conn, table_name=table_name, schema_name=schema_name
    )
    print(df_metabase_cards)
    # Step 2 : replace the column name and all its possible alias everywhere without taking into consideration
    # the case where multiple columns coming from diverse tables have the same named and are used.
    for index, row in df_metabase_cards.iterrows():
        update_report_card_with_new_column(conn, old_column_name, new_column_name, row)

    return
