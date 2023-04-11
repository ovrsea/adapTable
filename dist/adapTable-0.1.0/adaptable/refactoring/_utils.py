from adaptable._data_access.get_dataset_from_db import select_table, alter_table
import json


def retrieve_the_metabase_field_id_of_a_column(
    conn, column_name, schema_name, table_name
):
    variables = dict(
        {
            "table_name": table_name,
            "column_name": column_name,
            "schema_name": schema_name,
        }
    )
    query_file_path = "adaptable/_data_access/query/get_metabase_field_id.sql"
    df_metabase_field_id = select_table(conn, query_file_path, variables)
    print(df_metabase_field_id)
    if len(df_metabase_field_id) == 0:
        raise Exception("Column is not well specified")
    if len(df_metabase_field_id) > 1:
        raise Exception("Column is not uniquely specified")
    else:
        return df_metabase_field_id.loc[0, "field_id"]


def retrieve_the_metabase_table_id_of_a_table(conn, schema_name, table_name):
    variables = dict(
        {
            "table_name": table_name,
            "schema_name": schema_name,
        }
    )
    query_file_path = "adaptable/_data_access/query/get_metabase_table_id.sql"
    df_metabase_field_id = select_table(conn, query_file_path, variables)
    print(df_metabase_field_id)
    if len(df_metabase_field_id) == 0:
        raise Exception("Table is not well specified")
    if len(df_metabase_field_id) > 1:
        raise Exception("Table is not uniquely specified")
    else:
        return df_metabase_field_id.loc[0, "id"]


def retrieve_the_metabase_cards_using_sql_query_with_a_table(
    conn, schema_name, table_name
):
    variables = dict(
        {
            "table_name": table_name,
            "schema_name": schema_name,
        }
    )
    query_file_path = (
        "adaptable/_data_access/query/get_metabase_cards_with_specific_sql_query.sql"
    )
    df_metabase_fields = select_table(conn, query_file_path, variables)
    return df_metabase_fields


def delete_a_metabase_field_based_on_id(conn, metabase_field_id):
    variables = dict(
        {
            "metabase_field_id": int(metabase_field_id),
        }
    )
    query_file_path = (
        "adaptable/_data_access/deletion/delete_metabase_field_based_on_id.sql"
    )
    try:
        updated_row = alter_table(conn, query_file_path, variables)
        if updated_row == 0:
            raise Exception("No row deleted")
        if updated_row > 1:
            raise Exception("More than one row deleted")
        else:
            print("Deletion of metabase field work")
            return
    except Exception as e:
        print(e)


def delete_a_metabase_field_based_on_schema(conn, schema_name):
    variables = dict(
        {
            "schema_name": schema_name,
        }
    )
    query_file_path = (
        "adaptable/_data_access/deletion/delete_metabase_table_based_on_schema_name.sql"
    )
    try:
        updated_row = alter_table(conn, query_file_path, variables)
        print(
            "Deletion: {} tables reference have been deleted with the schema name given".format(
                updated_row
            )
        )
        return
    except Exception as e:
        print(e)


def delete_a_metabase_table_based_on_id(conn, metabase_table_id):
    variables = dict(
        {
            "metabase_table_id": int(metabase_table_id),
        }
    )
    query_file_path = (
        "adaptable/_data_access/deletion/delete_metabase_table_based_on_id.sql"
    )
    try:
        updated_row = alter_table(conn, query_file_path, variables)
        if updated_row == 0:
            raise Exception("No row deleted")
        if updated_row > 1:
            raise Exception("More than one row deleted")
        else:
            print("Deletion of metabase table work")
            return
    except Exception as e:
        print(e)


def change_the_id_of_one_metabase_field_row(
    conn, metabase_field_id_for_selection, metabase_field_id_of_replacement
):
    variables = dict(
        {
            "metabase_field_id_for_selection": int(metabase_field_id_for_selection),
            "metabase_field_id_of_replacement": int(metabase_field_id_of_replacement),
        }
    )
    query_file_path = "adaptable/_data_access/update/update_metabase_field_id_value.sql"
    try:
        updated_row = alter_table(conn, query_file_path, variables)
        if updated_row == 0:
            raise Exception("No row updated")
        if updated_row > 1:
            raise Exception("More than one row updated")
        else:
            print("Update of metabase field work")
            return
    except Exception as e:
        print(e)


def replace_column_name_in_query(sql_query_string, old_column_name, new_column_name):
    updated_sql_query_string = sql_query_string.replace(
        old_column_name, new_column_name
    )
    print(updated_sql_query_string)
    return updated_sql_query_string


def rename_table_and_activate_metabase_table(
    conn, new_table_name, new_display_table_name, old_table_id
):
    variables = dict(
        {
            "new_table_name": new_table_name,
            "new_display_table_name": new_display_table_name,
            "old_table_id": int(old_table_id),
        }
    )
    query_file_path = (
        "adaptable/_data_access/update/update_table_name_in_metabase_table.sql"
    )
    try:
        updated_row = alter_table(conn, query_file_path, variables)
        if updated_row == 0:
            raise Exception("No row updated")
        if updated_row > 1:
            raise Exception("More than one row updated")
        else:
            print("Update of metabase table work")
            return
    except Exception as e:
        print(e)


def replace_query_in_dataset_query_json(
    dataset_query_json, old_sql_query_string, updated_sql_query_string
):
    updated_dataset_query_json = dataset_query_json.replace(
        repr(old_sql_query_string), repr(updated_sql_query_string)
    )  # repr is a function that enables you to consider the string as completely raw and so here
    #  the character \n is not interpreted as a new line but is saved as it is. Without this command we would lost the format of the string
    # saved in the json and so won't be able to replace it.
    return updated_dataset_query_json


def update_report_card_with_new_column(
    conn, old_column_name, new_column_name, report_card_row
):
    dataset_query_json = report_card_row["dataset_query"]
    old_sql_query_string = json.loads(report_card_row["dataset_query"])["native"][
        "query"
    ]
    print(dataset_query_json)
    print(old_sql_query_string)

    updated_sql_query_string = replace_column_name_in_query(
        old_sql_query_string, old_column_name, new_column_name
    )
    updated_dataset_query_json = replace_query_in_dataset_query_json(
        dataset_query_json, old_sql_query_string, updated_sql_query_string
    )
    print(updated_dataset_query_json)

    variables = dict(
        {
            "report_card_id": report_card_row["id"],
            "updated_dataset_query_json": updated_dataset_query_json,
        }
    )
    query_file_path = (
        "adaptable/_data_access/update/update_column_name_in_sql_query.sql"
    )
    try:
        updated_row = alter_table(conn, query_file_path, variables)
        if updated_row == 0:
            raise Exception("No row updated")
        if updated_row > 1:
            raise Exception("More than one row updated")
        else:
            print("Update of report card worked")
            return
    except Exception as e:
        print(e)

    return


def update_schema_name_for_all_tables(conn, old_schema_name, new_schema_name):
    variables = dict(
        {
            "old_schema_name": old_schema_name,
            "new_schema_name": new_schema_name,
        }
    )
    query_file_path = (
        "adaptable/_data_access/update/update_metabase_table_schema_name.sql"
    )
    try:
        updated_row = alter_table(conn, query_file_path, variables)
        if updated_row == 0:
            raise Exception("No table found with the old schema name")
        else:
            print(
                "Update: {} tables reference have been updated with the new schema name".format(
                    updated_row
                )
            )
    except Exception as e:
        print(e)

    return
