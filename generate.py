from typing import TypedDict

import yaml

STATIC_ELEMENTS = {
    "<undoc/>": (
        "undoc",
        (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"'
            ' width="20" height="20"><path fill-rule="evenodd" d="M8 16A8 8 0 108 0a8 8 0 000'
            " 16zM5.5 4A1.5 1.5 0 004 5.5v5c0 .828.5 1.5 1 1.5v-1a1 1 0"
            " 011-1h5v1h-1v1h1.5a.5.5 0 00.5-.5v-7a.5.5 0 00-.5-.5h-6zm.5"
            " 7.25a.25.25 0 01.25-.25H9v2.764a.25.25 0 01-.426.178l-.898-.888a.25.25"
            ' 0 00-.352 0l-.898.888A.25.25 0 016 13.764V11.25z"></path></svg>'
        ),
    ),
    "<nobot/>": (
        "nobot",
        (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"'
            ' width="20" height="20"><path fill-rule="evenodd" d="M8 16A8 8 0 108 0a8 8 0 000'
            " 16zm.847-8.145a2.502 2.502 0 10-1.694 0C5.471 8.261 4 9.775 4 11c0"
            " .395.145.995 1 .995h6c.855 0 1-.6 1-.995"
            ' 0-1.224-1.47-2.74-3.153-3.145z"></path></svg>'
        ),
    ),
    "<iandeploy/>": (
        "iandeploy",
        (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"'
            ' width="20" height="20"><path fill-rule="evenodd" d="M8 16A8 8 0 108 0a8 8 0 000'
            " 16zm3.031-12a4.38 4.38 0 00-3.097"
            " 1.283l-.23.229c-.156.157-.308.32-.452.49H5.65a.876.876 0"
            " 00-.746.417l-.856 1.388a.375.375 0 00.21.556l1.552.477 1.35 1.35.478"
            " 1.553a.375.375 0 00.555.21l1.389-.855a.876.876 0"
            " 00.416-.746V8.747c.17-.144.333-.295.49-.452l.23-.23A4.38 4.38 0"
            " 0012 4.969v-.093A.876.876 0 0011.124 4h-.093zm-5.107 7.144a.81.81 0"
            " 01-.188.263c-.394.394-1.258.563-1.62.619a.124.124 0"
            ' 01-.143-.143c.056-.362.225-1.226.62-1.62a.808.808 0 011.33.881z"></path></svg>'
        ),
    ),
    "<nouser/>": (
        "nouser",
        (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"'
            ' width="20" height="20"><path fill-rule="evenodd" d="M2.343 13.657A8 8 0'
            " 1113.657 2.343 8 8 0 012.343 13.657zM6.03 4.97a.75.75 0 00-1.06 1.06L6.94"
            " 8 4.97 9.97a.75.75 0 101.06 1.06L8 9.06l1.97 1.97a.75.75 0"
            " 101.06-1.06L9.06 8l1.97-1.97a.75.75 0 10-1.06-1.06L8 6.94"
            ' 6.03 4.97z"></path></svg>'
        ),
    ),
}

Config = TypedDict(
    "Config", {"x-display-name": str, "x-description": str, "members": list[str]}
)

Method = TypedDict(
    "Method",
    {"x-display-name": str, "x-description": str, "x-body": str, "x-response": str},
)

MD_TEMPLATE = """### {name}

<details>

<summary>

<{method}>**{endpoint}**</{method}>

</summary>

<div class="d-content">

### Description

{description}

### Body

{body}

### Response

{response}

</div>

</details>

"""


def render(file: dict[str, str | dict[str, Method]]) -> str:
    data = f'## {file.pop("x-display-name")}\n\n{file.pop("x-description")}\n'

    file: dict[str, dict[str, Method]] = file

    for (endpoint, methods) in file.items():
        print(endpoint)
        for (method, meth_conf) in methods.items():
            data += MD_TEMPLATE.format(
                endpoint=endpoint,
                method=method.lower(),
                name=meth_conf["x-display-name"],
                description=meth_conf["x-description"],
                body=meth_conf["x-body"],
                response=meth_conf["x-response"],
            )

    return data


def generate_markdown_but_its_half_html():
    config: dict[str, Config]

    with open("./endpoints/config.yaml", "r") as conf:
        config = yaml.safe_load(conf)

    for (section, sec_conf) in config.items():
        data = f'# {sec_conf["x-display-name"]}\n\n{sec_conf["x-description"]}\n'
        for file in sec_conf["members"]:
            with open(f"./endpoints/{section}/{file}.yaml", "r") as f:
                data += render(yaml.safe_load(f.read()))
        with open(f"./book/endpoints/{section}.md", "w") as md:
            md.write(data)


if __name__ == "__main__":
    generate_markdown_but_its_half_html()
