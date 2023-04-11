UPDATE public.report_card
SET dataset_query = %(updated_dataset_query_json)s
WHERE id = %(report_card_id)s;