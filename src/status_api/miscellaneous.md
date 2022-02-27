# Miscellaneous

#### Base URL: `https://discordstatus.com/`

### {::get components.json}

These are the fancy little components displayed at the beginning of the status page.

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
