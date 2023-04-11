UPDATE public.metabase_field
SET id = %(metabase_field_id_of_replacement)s
WHERE id = %(metabase_field_id_for_selection)s;