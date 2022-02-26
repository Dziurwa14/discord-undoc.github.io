# Status API

#### Base URL: `https://discordstatus.com/api/v2/`

## Components

These are the fancy little components displayed at the beginning of the status page.

### {::get components.json}

Returns the components to be displayed.

{::details 
Response<summ>
```json
{
    "page": {
        "id": "srhpyqt94yxb",
        "name": "Discord",
        "url": "https://discordstatus.com",
        "time_zone": "America/Tijuana",
        "updated_at": "2022-02-15T13:37:37.407-08:00"
    },
    "components": [
        {
            "id": "rhznvxg4v7yh",
            "name": "API",
            "status": "operational",
            "created_at": "2015-07-30T18:55:43.739-07:00",
            "updated_at": "2022-02-15T13:21:55.150-08:00",
            "position": 1,
            "description": "The API is responsible for sending and receiving messages, and general operations on the platform. If this is down, chances are you'll have trouble connecting and/or sending messages.",
            "showcase": true,
            "start_date": null,
            "group_id": null,
            "page_id": "srhpyqt94yxb",
            "group": false,
            "only_show_if_degraded": false
        }
    ]
}
```
}

## Incidents

Incidents, these are followed by an Ian 2 deploy {::iandeploy} /j

<br>

**Status**: *Investigating, Identified, Monitoring, Resolved, or Postmortem*\
**Impact**: *None (black), Minor (yellow), Major (orange), or Critical (red)*

### {::get incidents.json}

Returns up-to 50 recent incidents. This endpoint returns **all** incidents no matter the status.

{::details 
Response<summ>
```json
{
    "page": {
        "id": "srhpyqt94yxb",
        "name": "Discord",
        "url": "https://discordstatus.com",
        "time_zone": "America/Tijuana",
        "updated_at": "2022-02-15T13:37:37.407-08:00"
    },
    "incidents": [
        {
            "id": "n4njzfn1mqy0",
            "name": "Messaging issues",
            "status": "resolved",
            "created_at": "2022-02-15T13:14:17.744-08:00",
            "updated_at": "2022-02-15T13:37:37.404-08:00",
            "monitoring_at": "2022-02-15T13:21:55.183-08:00",
            "resolved_at": "2022-02-15T13:37:37.388-08:00",
            "impact": "minor",
            "shortlink": "https://stspg.io/y1w39cblgvhz",
            "started_at": "2022-02-15T13:14:17.737-08:00",
            "page_id": "srhpyqt94yxb",
            "incident_updates": [
                {
                    "id": "7gv6pn1zyz2n",
                    "status": "investigating",
                    "body": "We're investigating high latency related to channels and messages.",
                    "incident_id": "n4njzfn1mqy0",
                    "created_at": "2022-02-15T13:14:17.849-08:00",
                    "updated_at": "2022-02-15T13:14:17.849-08:00",
                    "display_at": "2022-02-15T13:14:17.849-08:00",
                    "affected_components": [
                        {
                            "code": "rhznvxg4v7yh",
                            "name": "API",
                            "old_status": "operational",
                            "new_status": "degraded_performance"
                        }
                    ],
                    "deliver_notifications": true,
                    "custom_tweet": null,
                    "tweet_id": null
                }
            ],
            "components": [
                {
                    "id": "rhznvxg4v7yh",
                    "name": "API",
                    "status": "operational",
                    "created_at": "2015-07-30T18:55:43.739-07:00",
                    "updated_at": "2022-02-15T13:21:55.150-08:00",
                    "position": 1,
                    "description": "The API is responsible for sending and receiving messages, and general operations on the platform. If this is down, chances are you'll have trouble connecting and/or sending messages.",
                    "showcase": true,
                    "start_date": null,
                    "group_id": null,
                    "page_id": "srhpyqt94yxb",
                    "group": false,
                    "only_show_if_degraded": false
                }
            ]
        }
    ]
}
```
}

### {::get incidents/unresolved.json}

Returns information on unresolved incidents.

Only returns incidents that are in the following state:
- Investigating
- Identified
- Monitoring

{::details 
Response<summ>
```json
{
    "page": {
        "id": "srhpyqt94yxb",
        "name": "Discord",
        "url": "https://discordstatus.com",
        "time_zone": "America/Tijuana",
        "updated_at": "2022-02-15T13:37:37.407-08:00"
    },
    "incidents": []
}
```
}

## Scheduled Maintenances

Quote from official status api docs:
> Scheduled maintenances are planned outages, upgrades, or general notices that we're working on infrastructure and disruptions may occurr.

### {::get scheduled-maintenances.json}

Returns up-to 50 recent scheduled maintenances. The result includes both scheduled and "Completed" maintenances.

{::details 
Response<summ>
```json
{
    "page": {
        "id": "srhpyqt94yxb",
        "name": "Discord",
        "url": "https://discordstatus.com",
        "time_zone": "America/Tijuana",
        "updated_at": "2022-02-15T13:37:37.407-08:00"
    },
    "scheduled_maintenances": [
        {
            "id": "chkt3cr0jf7b",
            "name": "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Server Juice",
            "status": "completed",
            "created_at": "2015-09-18T18:20:40.535-07:00",
            "updated_at": "2015-09-22T02:25:20.086-07:00",
            "monitoring_at": "2015-09-22T01:07:50.805-07:00",
            "resolved_at": "2015-09-22T02:25:20.034-07:00",
            "impact": "major",
            "shortlink": "http://stspg.io/1UdW",
            "started_at": "2015-09-18T18:20:00.000-07:00",
            "page_id": "srhpyqt94yxb",
            "incident_updates": [
                {
                    "id": "1nz6l9z9fbyc",
                    "status": "scheduled",
                    "body": "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Wow our servers wow. They're getting so much juice wow. Please wait while we give them juice (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧\r\n\r\nWe're powering up our servers to handle more fabulous Discord people 〜(￣▽￣〜)\r\n\r\nOn a serious note, we worked hard to attempt to do this without downtime, but have come to the conclusion it would be impossible.",
                    "incident_id": "chkt3cr0jf7b",
                    "created_at": "2015-09-18T18:20:40.794-07:00",
                    "updated_at": "2015-09-19T15:45:59.626-07:00",
                    "display_at": "2015-09-18T18:20:00.000-07:00",
                    "affected_components": null,
                    "deliver_notifications": true,
                    "custom_tweet": null,
                    "tweet_id": null
                }
            ],
            "components": [],
            "scheduled_for": "2015-09-22T01:00:00.000-07:00",
            "scheduled_until": "2015-09-22T01:30:00.000-07:00"
        }
    ]
}
```
}

### {::get scheduled-maintenances/active.json}

Returns active scheduled maintenances.

Only includes the following states:
- In Progress
- Verifying

{::details 
Response<summ>
```json
{
    "page": {
        "id": "srhpyqt94yxb",
        "name": "Discord",
        "url": "https://discordstatus.com",
        "time_zone": "America/Tijuana",
        "updated_at": "2022-02-15T13:37:37.407-08:00"
    },
    "scheduled_maintenances": []
}
```
}

### {::get scheduled-maintenances/upcoming.json}

Returns maintenances that are still in the "Scheduled" state.

{::details 
Response<summ>
```json
{
    "page": {
        "id": "srhpyqt94yxb",
        "name": "Discord",
        "url": "https://discordstatus.com",
        "time_zone": "America/Tijuana",
        "updated_at": "2022-02-15T13:37:37.407-08:00"
    },
    "scheduled_maintenances": []
}
```
}

# Miscellaneous

### {::get status.json}

Returns information on the current status of the API. Contains a description for further information.

{::details 
Response<summ>
```json
{
    "page": {
        "id": "srhpyqt94yxb",
        "name": "Discord",
        "url": "https://discordstatus.com",
        "time_zone": "America/Tijuana",
        "updated_at": "2022-02-15T13:37:37.407-08:00"
    },
    "status": {
        "indicator": "none",
        "description": "All Systems Operational"
    }
}
```
}

### {::get summary.json}

A summary of the page, contains:
- Status
- Components
- Incidents
- Scheduled Maintenances

{::details 
Response<summ>
```json
{
    "page": {
        "id": "srhpyqt94yxb",
        "name": "Discord",
        "url": "https://discordstatus.com",
        "time_zone": "America/Tijuana",
        "updated_at": "2022-02-15T13:37:37.407-08:00"
    },
    "components": [
        {
            "id": "qk867vbbh84x",
            "name": "South Korea",
            "status": "operational",
            "created_at": "2020-08-30T03:42:44.139-07:00",
            "updated_at": "2020-08-30T09:16:24.968-07:00",
            "position": 9,
            "description": null,
            "showcase": false,
            "start_date": null,
            "group_id": "jk03xttfcz9b",
            "page_id": "srhpyqt94yxb",
            "group": false,
            "only_show_if_degraded": false
        }
    ],
    "incidents": [],
    "scheduled_maintenances": [],
    "status": {
        "indicator": "none",
        "description": "All Systems Operational"
    }
}
```
}

<br>

# Metrics

These endpoints return API response time metrics for the particular day|week|month.

You'll ony see spikes in these numbers when {::user Desch#3091-90339695967350784-ab775dfe83d1a8057587a837eedde447} commits to `discord/discord@master`

#### Base URL: `https://discordstatus.com/`

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
