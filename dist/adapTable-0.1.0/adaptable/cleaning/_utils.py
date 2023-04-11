from adaptable._data_access.get_dataset_from_db import select_table, alter_table


def retrieve_the_metabase_card_id_of_not_recently_looked_at_card(
    conn, freshness_in_month: int
):
    variables = dict(
        {
            "freshness_in_month": freshness_in_month,
        }
    )
    query_file_path = (
        "adaptable/_data_access/query/get_metabase_cards_not_recently_looked_at.sql"
    )
    df_metabase_card_id = select_table(conn, query_file_path, variables)
    print(df_metabase_card_id)
    return df_metabase_card_id


def retrieve_the_metabase_dashboard_id_of_not_recently_looked_at_dashboard(
    conn, freshness_in_month: int
):
    variables = dict(
        {
            "freshness_in_month": freshness_in_month,
        }
    )
    query_file_path = (
        "adaptable/_data_access/query/get_metabase_dashboard_not_recently_looked_at.sql"
    )
    df_metabase_dashboard_id = select_table(conn, query_file_path, variables)
    print(df_metabase_dashboard_id)
    return df_metabase_dashboard_id


def delete_report_dashboardcard_on_card_id(conn, card_id_list: list):
    variables = dict(
        {
            "card_id_list": tuple(card_id_list),
        }
    )
    query_file_path = "adaptable/_data_access/deletion/delete_report_dashboardcard_on_chosen_card_id.sql"
    try:
        updated_row = alter_table(conn, query_file_path, variables)
        if updated_row == 0:
            raise Exception("No row updated")
        else:
            print(
                "Deletion: {} report_dashboarcard rows have been deleted".format(
                    updated_row
                )
            )
            return
    except Exception as e:
        print(e)


def archived_report_cards_using_id_list(conn, card_id_list: list):
    variables = dict(
        {
            "card_id_list": tuple(card_id_list),
        }
    )
    query_file_path = (
        "adaptable/_data_access/update/archive_report_cards_using_id_list.sql"
    )
    try:
        updated_row = alter_table(conn, query_file_path, variables)
        if updated_row == 0:
            raise Exception("No row updated")
        else:
            print("Update: {} report_card rows have been archived".format(updated_row))
            return
    except Exception as e:
        print(e)


def archived_report_dashboards_using_id_list(conn, dashboard_id_list: list):
    variables = dict(
        {
            "dashboard_id_list": tuple(dashboard_id_list),
        }
    )
    query_file_path = (
        "adaptable/_data_access/update/archive_report_dashboards_using_id_list.sql"
    )
    try:
        updated_row = alter_table(conn, query_file_path, variables)
        if updated_row == 0:
            raise Exception("No row updated")
        else:
            print(
                "Update: {} report_dashboard rows have been archived".format(
                    updated_row
                )
            )
            return
    except Exception as e:
        print(e)
