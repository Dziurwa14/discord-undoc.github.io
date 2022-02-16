# Unofficial Discord Documentation

Main repository for the Discord-Undoc website, the documentation lives in `./src`\
The website can be found at https://discord-undoc.github.io

## How do I contribute?

> NOTE: You cannot preview the documenation without the `./theme` folder!

**Prerequisites**
1. Rust
2. Cargo
3. mdbook (can be installed by `cargo install mdbook`)
4. Python
5. Poetry (optional)
6. mistletoe (can be installed by `pip install mistletoe`
   or if you have poetry you can `poetry install` this also installs dev deps)

After installing `mdbook` go ahead and grab the latest iteration of the theme.

If you are on unix:
```bash
$ chmod +x ./get_theme.sh
$ ./get_theme.sh
```

If you are on windows:
*Unfortunately we don't have a script for windows yet, you have to manually downlaod the
theme from the [`/discord-undoc/discord-undoc-theme`](https://github.com/discord-undoc/discord-undoc-theme) repository.*

Once you have the theme, you can start editing the files.\
Make sure to start your mdbook server to see the changes live!
— Can be done by `mdbook serve`
