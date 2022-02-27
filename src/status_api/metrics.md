# Metrics

#### Base URL: `https://discordstatus.com/`

These endpoints return API response time metrics for the particular day|week|month.

You'll ony see spikes in these numbers when {::user Desch#3091-90339695967350784-ab775dfe83d1a8057587a837eedde447} commits to `discord/discord@master`

### {::get metrics-display/5k2rt9f7pmny/day.json {::undoc}}

{::details 
Response<summ>
```json
{
    "period": {
        "count": 288,
        "interval": 300,
        "identifier": "day"
    },
    "metrics": [
        {
            "metric": {
                "name": "API Response Time",
                "metric_identifier": "avg:discord_api.http.response_time.avg{*}",
                "created_at": "2016-07-19T23:14:15.396Z",
                "updated_at": "2016-07-19T23:14:15.396Z",
                "id": "pbb6x1yjh8s3",
                "metrics_provider_id": "4l4nqp7hhz9c",
                "metrics_display_id": "5k2rt9f7pmny",
                "most_recent_data_at": "2022-02-19T19:07:30.000Z",
                "backfilled": true,
                "last_fetched_at": "2022-02-19T19:07:49.162Z",
                "backfill_percentage": 1.0
            },
            "summary": {
                "sum": 18942.690741995844,
                "mean": 65.77323174304114
            },
            "data": [
                {
                    "timestamp": 1645211400,
                    "value": 75
                }
            ]
        }
    ],
    "summary": {
        "sum": 18942.690741995844,
        "mean": 65.77323174304114,
        "last": 71
    }
}
```
}

### {::get metrics-display/5k2rt9f7pmny/month.json {::undoc}}

{::details 
Response<summ>
```json
{
    "period": {
        "count": 336,
        "interval": 7200,
        "identifier": "month"
    },
    "metrics": [
        {
            "metric": {
                "name": "API Response Time",
                "metric_identifier": "avg:discord_api.http.response_time.avg{*}",
                "created_at": "2016-07-19T23:14:15.396Z",
                "updated_at": "2016-07-19T23:14:15.396Z",
                "id": "pbb6x1yjh8s3",
                "metrics_provider_id": "4l4nqp7hhz9c",
                "metrics_display_id": "5k2rt9f7pmny",
                "most_recent_data_at": "2022-02-19T19:07:30.000Z",
                "backfilled": true,
                "last_fetched_at": "2022-02-19T19:07:49.162Z",
                "backfill_percentage": 1.0
            },
            "summary": {
                "sum": 27081.61790839434,
                "mean": 81.0826883484861
            },
            "data": [
                {
                    "timestamp": 1642881600,
                    "value": 81
                }
            ]
        }
    ],
    "summary": {
        "sum": 27081.61790839434,
        "mean": 81.0826883484861,
        "last": 67
    }
}
```
}

### {::get metrics-display/5k2rt9f7pmny/week.json {::undoc}}

{::details 
Response<summ>
```json
{
    "period": {
        "count": 336,
        "interval": 1800,
        "identifier": "week"
    },
    "metrics": [
        {
            "metric": {
                "name": "API Response Time",
                "metric_identifier": "avg:discord_api.http.response_time.avg{*}",
                "created_at": "2016-07-19T23:14:15.396Z",
                "updated_at": "2016-07-19T23:14:15.396Z",
                "id": "pbb6x1yjh8s3",
                "metrics_provider_id": "4l4nqp7hhz9c",
                "metrics_display_id": "5k2rt9f7pmny",
                "most_recent_data_at": "2022-02-19T19:07:30.000Z",
                "backfilled": true,
                "last_fetched_at": "2022-02-19T19:07:49.162Z",
                "backfill_percentage": 1.0
            },
            "summary": {
                "sum": 26279.883939332976,
                "mean": 77.98185145202665
            },
            "data": [
                {
                    "timestamp": 1644692400,
                    "value": 88
                }
            ]
        }
    ],
    "summary": {
        "sum": 26279.883939332976,
        "mean": 77.98185145202665,
        "last": 72
    }
}
```
}
