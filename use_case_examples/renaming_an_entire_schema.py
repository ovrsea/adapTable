import psycopg2
from adaptable.refactoring.reference_system import renaming_card_schema

"""
At some point in refactoring, you might need to rename a schema in your own database.
By doing so you will break all the custom question that were using tables coming from this schema.
Here is a way to fix all your custom questions. 

First you should already have : 
- created the new schema in your database
- Have triggered a Metabase scan of your database
"""

old_schema_name = "wrongly_named_schema"
new_schema_name = "well_named_schema"
conn = psycopg2.connect()  # To complete with your Metabase db connection
renaming_card_schema(conn, old_schema_name, new_schema_name)

if conn is not None:
    conn.close()
