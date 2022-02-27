# Incidents

#### Base URL: `https://discordstatus.com/`

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
