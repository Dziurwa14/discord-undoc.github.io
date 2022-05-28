from typing import Literal, TypedDict
from yaml import safe_load

Config = TypedDict(
    "Config",
    {
        "x-section-name": str,
        "x-display-name": str,
        "x-description": str,
        "members": list[str],
    },
)

Method = TypedDict(
    "Method",
    {
        "x-indicators": str,
        "x-display-name": str,
        "x-description": str,
        "x-body": str,
        "x-query": str,
        "x-response": str,
    },
)


def generate_list():
    config: list[dict[str, Config]]
    data: list[str] = []

    with open("endpoints/config.yaml", "r") as conffile:
        config = safe_load(conffile)

    for section in config:
        for member in section["members"]:
            with open(
                f"endpoints/{section['x-section-name']}/{member}.yaml", "r"
            ) as file:
                member_file: dict[
                    str,
                    dict[
                        Literal[
                            "unknown",
                            "under development",
                            "get",
                            "head",
                            "post",
                            "put",
                            "delete",
                            "connect",
                            "options",
                            "trace",
                            "patch",
                        ],
                        dict[str, Method],
                    ],
                ] = safe_load(file)

                # Shittiest code in human history

                data.extend(
                    list(
                        map(
                            lambda kv: f"`{kv[0]}` - `{kv[1]}`",
                            dict(
                                zip(
                                    member_file.keys(),
                                    map(
                                        lambda methods: ", ".join(
                                            methods.keys()
                                        ).upper(),
                                        member_file.values(),
                                    ),
                                )
                            ).items(),
                        )
                    )
                )

    data.sort()

    return data


if __name__ == "__main__":
    print(
        r"""# Endpoints List

## Base URLs

**Base API URL** - `https://canary.discord.com/api/v9/`\
**Base Status API URL** - `https://discordstatus.com/api/v2/` or `https://discordstatus.com/`

## Endpoints
"""
    )
    print("-", "\n- ".join(generate_list()))
    print(
        """
## Status API

- `components.json`
- `incidents.json`
- `incidents/unresolved.json`
- `metrics-display/5k2rt9f7pmny/day.json`
- `metrics-display/5k2rt9f7pmny/month.json`
- `metrics-display/5k2rt9f7pmny/week.json`
- `scheduled-maintenances.json`
- `scheduled-maintenances/active.json`
- `scheduled-maintenances/upcoming.json`
- `status.json`
- `summary.json`"""
    )
