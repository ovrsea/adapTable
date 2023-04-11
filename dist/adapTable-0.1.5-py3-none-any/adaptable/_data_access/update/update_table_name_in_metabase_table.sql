UPDATE public.metabase_table
SET name = %(new_table_name)s,
    display_name = %(new_display_table_name)s,
    active = True
WHERE id = %(old_table_id)s;