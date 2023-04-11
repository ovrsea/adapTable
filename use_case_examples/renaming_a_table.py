import psycopg2
from adaptable.refactoring.reference_system import renaming_card_table

"""
At some point in refactoring, you might need to rename a table in your own database.
By doing so you will break all the custom questions that were using this table.
Here is a way to fix all your custom questions.

First you should already have : 
- created the new table in your database
- Have triggered a Metabase scan of your database 
"""

old_table_name = "wrongly_named_table"
new_table_name = "well_named_table"
new_display_table_name = "Well Named Table"
# Note : for the displayed name, you should follow the standard of Metabase, meaning :
# - "_" should translated as a blank space
# - All the world should start with a capital letter
# Example : well_named_table is Well Named Table
schema_name = "schema_shared_by_wrongly_and_well_named_tables"
# Note : As it is meant only to rename a table, before triggering this script the new table name should have been
# created.


conn = psycopg2.connect()  # To complete with your Metabase db connection
renaming_card_table(
    conn,
    old_table_name,
    new_table_name,
    new_display_table_name,
    schema_name,
)

if conn is not None:
    conn.close()
