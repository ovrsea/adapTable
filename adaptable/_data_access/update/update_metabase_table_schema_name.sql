UPDATE public.metabase_table
SET schema = %(new_schema_name)s
WHERE schema = %(old_schema_name)s;