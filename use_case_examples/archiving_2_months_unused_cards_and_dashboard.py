import psycopg2
from adaptable.cleaning.archiving import (
    archiving_unused_cards,
    archiving_unused_dashboards,
)

"""
If a lof of your cards and dashboards are not looked at frequently enough
you might want to archive them based on the fact that they were not 
used in the last 2 months. Here is the code to do that. 
"""

# Limit in number of month for a dashboard or card unlooked at to be considered as unused and so archived.
nb_of_month = 2


conn = psycopg2.connect()  # To complete with your Metabase db connection
archiving_unused_cards(conn, nb_of_month)
archiving_unused_dashboards(conn, nb_of_month)


if conn is not None:
    conn.close()
