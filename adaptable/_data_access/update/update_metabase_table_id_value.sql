UPDATE public.metabase_table
SET id = %(metabase_table_id_of_replacement)s
WHERE id = %(metabase_table_id_for_selection)s;