from adaptable.cleaning._utils import (
    retrieve_the_metabase_card_id_of_not_recently_looked_at_card,
    retrieve_the_metabase_dashboard_id_of_not_recently_looked_at_dashboard,
    delete_report_dashboardcard_on_card_id,
    archived_report_cards_using_id_list,
    archived_report_dashboards_using_id_list,
)


def archiving_unused_cards(conn, freshness_in_month: int):
    """Archiving cards that were not looked at in the last months both through dashboard or direct observation.

    Parameters
    ----------
    conn: psycopg2 DBAPI2 connector
        Connexion to your Metabase Database
    freshness_in_month : int
        The minimal last seen period in month required for a card not to be archived as considered useless.

    Returns
    -------
    Nothing as it has been build to change the Metabase DB synchronously.
    """
    # Step 1: Found all the cards unused in the delay_in_month
    df_metabase_card_id = retrieve_the_metabase_card_id_of_not_recently_looked_at_card(
        conn, freshness_in_month
    )
    print(df_metabase_card_id)
    card_id_list = df_metabase_card_id["id"]
    # Step 2: Remove the row that call the id_ concerned from metabase_dashboard_cards
    delete_report_dashboardcard_on_card_id(conn, card_id_list)

    # Step 3: Archived the row in report_cards
    archived_report_cards_using_id_list(conn, card_id_list)

    return


def archiving_unused_dashboards(conn, freshness_in_month):
    """Archiving dashboards that were not looked at once in the last months.

    Parameters
    ----------
    conn: psycopg2 DBAPI2 connector
        Connexion to your Metabase Database
    freshness_in_month : int
        The minimal last seen period in month required for a card not to be archived as considered useless.

    Returns
    -------
    Nothing as it has been build to change the Metabase DB synchronously.
    """
    # Step 1: Found all the dashboards unused in the delay_in_month
    df_metabase_dashboard_id = (
        retrieve_the_metabase_dashboard_id_of_not_recently_looked_at_dashboard(
            conn, freshness_in_month
        )
    )
    print(df_metabase_dashboard_id)
    dashboard_id_list = df_metabase_dashboard_id["id"]

    # Step 2: Archived the row in report_dashboards
    archived_report_dashboards_using_id_list(conn, dashboard_id_list)

    return
