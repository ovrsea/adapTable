WITH recently_viewed_dashboard AS (
    SELECT DISTINCT(model_id)
    FROM public.view_log
    WHERE model = 'dashboard'
      AND timestamp > CURRENT_DATE - INTERVAL '%(freshness_in_month)s MONTH'
    GROUP BY id)
SELECT report_dashboard.id
FROM public.report_dashboard
         LEFT JOIN recently_viewed_dashboard
                   ON recently_viewed_dashboard.model_id = report_dashboard.id
WHERE recently_viewed_dashboard.model_id IS NULL
  AND archived = FALSE