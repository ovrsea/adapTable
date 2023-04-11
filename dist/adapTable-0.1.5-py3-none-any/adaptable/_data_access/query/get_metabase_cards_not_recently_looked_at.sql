WITH recently_viewed_card AS (
    SELECT DISTINCT(model_id)
    FROM public.view_log
    WHERE model = 'card'
      AND timestamp > CURRENT_DATE - INTERVAL '%(freshness_in_month)s MONTH'
    GROUP BY id),
     recently_view_dashboard_card AS (
         SELECT DISTINCT(report_dashboardcard.card_id)
         FROM report_dashboardcard
                  LEFT JOIN view_log
                            ON view_log.model_id = report_dashboardcard.dashboard_id
                                AND view_log.model = 'dashboard'
         WHERE view_log.timestamp > CURRENT_DATE - INTERVAL '%(freshness_in_month)s MONTH'
         GROUP BY card_id
     )
SELECT report_card.id
FROM public.report_card
         LEFT JOIN recently_viewed_card
                   ON recently_viewed_card.model_id = report_card.id
         LEFT JOIN recently_view_dashboard_card
                   ON recently_view_dashboard_card.card_id = report_card.id
WHERE recently_viewed_card.model_id IS NULL
  AND recently_view_dashboard_card.card_id IS NULL
  AND archived = FALSE