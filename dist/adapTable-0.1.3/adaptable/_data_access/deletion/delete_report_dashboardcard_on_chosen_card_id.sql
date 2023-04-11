DELETE FROM public.report_dashboardcard
WHERE card_id IN %(card_id_list)s;