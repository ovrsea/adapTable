SELECT dataset_query,
       id
FROM public.report_card
WHERE query_type = 'native'
AND dataset_query LIKE CONCAT('%%',%(schema_name)s,'.',%(table_name)s,'%%')