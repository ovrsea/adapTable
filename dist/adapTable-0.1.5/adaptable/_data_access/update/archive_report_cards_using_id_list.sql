UPDATE public.report_card
SET archived = TRUE
WHERE id IN %(card_id_list)s;