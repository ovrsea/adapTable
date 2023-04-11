DELETE FROM public.metabase_field
WHERE table_id = %(metabase_table_id)s;