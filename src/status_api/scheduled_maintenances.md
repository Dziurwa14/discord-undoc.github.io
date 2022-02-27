# Scheduled Maintenances

#### Base URL: `https://discordstatus.com/`

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
