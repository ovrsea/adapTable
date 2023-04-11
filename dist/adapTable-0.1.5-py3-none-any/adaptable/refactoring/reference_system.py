from adaptable.refactoring._utils import (
    retrieve_the_metabase_field_id_of_a_column,
    retrieve_the_metabase_table_id_of_a_table,
    delete_a_metabase_field_based_on_id,
    delete_a_metabase_field_based_on_schema,
    change_the_id_of_one_metabase_field_row,
    rename_table_and_activate_metabase_table,
    update_schema_name_for_all_tables,
)


def renaming_card_column(
    conn, old_column_name: str, new_column_name: str, table_name: str, schema_name: str
):
    """Renaming column in the ref system of Metabase, and thus is updating all the custom questions using this column

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

    # Fix the custom questions

    # Step 1: finding the id of the new and old columns in the metabase field table
    old_metabase_field_id = retrieve_the_metabase_field_id_of_a_column(
        conn=conn,
        column_name=old_column_name,
        table_name=table_name,
        schema_name=schema_name,
    )
    print(old_metabase_field_id)

    new_metabase_field_id = retrieve_the_metabase_field_id_of_a_column(
        conn=conn,
        column_name=new_column_name,
        table_name=table_name,
        schema_name=schema_name,
    )
    print(new_metabase_field_id)

    # Step 2: Delete the old column by removing a row in the metafield
    delete_a_metabase_field_based_on_id(conn, old_metabase_field_id)

    # Step 3: Change the id of the new column in the metafield to
    change_the_id_of_one_metabase_field_row(
        conn, new_metabase_field_id, old_metabase_field_id
    )

    return


def renaming_card_table(
    conn,
    old_table_name: str,
    new_table_name: str,
    new_display_table_name: str,
    schema_name: str,
):
    """Renaming table in the ref system of Metabase, and thus is updating all the custom questions using this table

    Parameters
    ----------
    conn: psycopg2 DBAPI2 connector
        Connexion to your Metabase Database
    old_table_name : str
        Former name of the table
    new_table_name : str
        New name of the table
    new_display_table_name : str
        New name of the displayed table. Should follow the standard : table_name has a displayed name "Table Name"
    schema_name : str
        Schema name that contains the column table

    Returns
    -------
    Nothing as it has been build to change the Metabase DB synchronously.
    """
    # PART 1: Fix the custom questions

    # Step 1: finding the id of the new and old table in the metabase_table table
    old_metabase_table_id = retrieve_the_metabase_table_id_of_a_table(
        conn=conn,
        table_name=old_table_name,
        schema_name=schema_name,
    )
    print(old_metabase_table_id)

    new_metabase_table_id = retrieve_the_metabase_table_id_of_a_table(
        conn=conn,
        table_name=new_table_name,
        schema_name=schema_name,
    )
    print(new_metabase_table_id)

    # Step 2: Delete the new table created by the sync of Metabase
    delete_a_metabase_table_based_on_id(conn, new_metabase_table_id)

    # Step 3: Update the old metabase ref to the table to rename it and re-activate it.
    rename_table_and_activate_metabase_table(
        conn,
        new_table_name,
        new_display_table_name,
        old_metabase_table_id,
    )

    return


def renaming_card_schema(conn, old_schema_name, new_schema_name):
    """Renaming schema in the ref system of Metabase

    Parameters
    ----------
    conn: psycopg2 DBAPI2 connector
        Connexion to your Metabase Database
    old_schema_name : str
        Former name of the schema
    new_schema_name : str
        New name of the schema

    Returns
    -------
    Nothing as it has been build to change the Metabase DB synchronously.
    """
    # Step 1: Remove ref tables of the new schema name to avoid key violation constraints
    delete_a_metabase_field_based_on_schema(conn, new_schema_name)
    # Step 2: Renaming in the column 'schema' of metabase_table : old_schema_name into new_schema_name
    update_schema_name_for_all_tables(conn, old_schema_name, new_schema_name)

    return
