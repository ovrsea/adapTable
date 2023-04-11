SELECT mf.id AS field_id,
       mf.name AS field_name,
       mf.table_id AS table_id,
       mt.name AS table_name,
       mt.schema AS schema_name
FROM public.metabase_field AS mf
LEFT JOIN public.metabase_table AS mt
ON mf.table_id = mt.id
WHERE mf.name = %(column_name)s
AND mt.name = %(table_name)s
AND mt.schema = %(schema_name)s