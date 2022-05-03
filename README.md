# Unofficial Discord Documentation

[![Discord](https://img.shields.io/discord/943759314856849468?style=flat-square&color=fd745e&label=Unofficial%20Discord%20Documentation&logo=discord&logoColor=FFFFFF&labelColor=36393F)](https://discord.gg/zVB5P96GE2)

Main repository for the Discord-Undoc website, the documentation lives in `./src`\
The website can be found at <https://discord-undoc.github.io>

## How do I contribute?

Make sure to read our [Contribution Guidelines](./.github/CONTRIBUTING.md) first!

### You need

1. Rust
2. mdbook
3. Python

Go ahead and grab the latest iteration of the theme.

If you are on unix:

```bash
$ chmod +x ./get_theme.sh
>
$ ./get_theme.sh
>
```

If you are on windows:
*Unfortunately we don't have a script for windows yet, you have to manually downlaod the
theme from the [`/discord-undoc/discord-undoc-theme`](https://github.com/discord-undoc/discord-undoc-theme) repository.*
or use something like git bash.

Once you have the theme, you can install the required dependencies; i.e:

- mistletoe
- httpx
- orjson
- beautifulsoup4

After this you can go ahead and start writing some documentation,\
dont forget to use `mdbook serve` for a live preview!
