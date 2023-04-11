SELECT id
FROM public.metabase_table
WHERE name = %(table_name)s
AND schema = %(schema_name)s