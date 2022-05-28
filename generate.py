"""Copyright 2022 한승민

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

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

NEW_LINE = "\n"


def render(
    file: dict[
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
    ]
) -> str:
    data = ""
    for (endpoint, methods) in file.items():
        print(f"Rendering '{endpoint}' with '{len(methods)}' methods")
        for (method, meth_conf) in methods.items():
            if method in {"unknown", "under development"}:
                continue

            data += f"""## {meth_conf['x-display-name']}

<{method}>{endpoint}</{method}>
{"" if len(meth_conf["x-indicators"]) == 0 else  NEW_LINE + " ".join(map(lambda x: f"<{x}></{x}>", meth_conf["x-indicators"])) + NEW_LINE}
<br>

**Description**

{meth_conf['x-description']}

<br>

**Body**

<br>

{meth_conf['x-body']}

<br>

**Queries**

<br>

{meth_conf['x-query']}

<br>

**Response**

<br>

{meth_conf['x-response']}

"""

    return data


def generate_markdown_but_its_half_html():
    config: list[Config]

    with open("endpoints/config.yaml", "r") as conffile:
        config = safe_load(conffile)

    for section in config:
        data = (
            f"# {section['x-display-name']}\n\n{section['x-description']}\n\n<br>\n\n"
        )
        for member in section["members"]:
            with open(
                f"endpoints/{section['x-section-name']}/{member}.yaml", "r"
            ) as file:
                data += render(safe_load(file))
        with open(f"src/endpoints/{section['x-section-name']}.md", "w") as md:
            md.write(data[:-1])


if __name__ == "__main__":
    generate_markdown_but_its_half_html()
