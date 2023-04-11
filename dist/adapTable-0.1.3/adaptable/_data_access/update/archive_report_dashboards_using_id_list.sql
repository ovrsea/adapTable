UPDATE public.report_dashboard
SET archived = TRUE
WHERE id IN %(dashboard_id_list)s;