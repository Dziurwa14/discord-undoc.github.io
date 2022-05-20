from typing import TypedDict
import yaml

Config = TypedDict(
    "Config", {"x-display-name": str, "x-description": str, "members": list[str]}
)

Method = TypedDict(
    "Method",
    {"x-display-name": str, "x-description": str, "x-body": str, "x-response": str},
)


def get_list(file: dict[str, str | dict[str, Method]]) -> list[str]:
    data = []

    file.pop("x-display-name")
    file.pop("x-description")

    file: dict[str, dict[str, Method]] = file

    data.extend(list(file))

    return data


def generate_list() -> list[str]:
    config: dict[str, Config]

    data: list[str] = []

    with open("./endpoints/config.yaml", "r") as conf:
        config = yaml.safe_load(conf)

    for (section, sec_conf) in config.items():
        for file in sec_conf["members"]:
            with open(f"./endpoints/{section}/{file}.yaml", "r") as f:
                data.extend(get_list(yaml.safe_load(f.read())))

    data.sort()

    return data


if __name__ == "__main__":
    print("\n".join(generate_list()))
