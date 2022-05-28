# Contribution

Other than the main team mentioned in the [FAQ](index.html#who-are-we)
the documentation is a community effort. Which means there are certain
rules, points, and notes that you need to follow before contributing.

## Wanted contributions

> - [x] Updating invalid links and/or information.
> - [x] Released features/changes that are not documented.
> - [x] Fixing invalid/outdated example snippets in the documentation.
> - [x] Fixing of spelling, grammatical errors and incorrect statements or inaccuracies in the documentation.
> - [x] Cats

## Unwanted contributions

> - [ ] Adding invalid and/or unverified information.
> - [ ] Adding misleading information.
> - [ ] Removing whitespace.
> - [ ] Modifications to the overall structure and format of the documentation.

## Basic contribution guidelines

- Install & Setup Rust.
- Install mdbook via `cargo install mdbook`.
- Install & Setup python (used for utilities).

Clone this (discord-undoc.github.io) repository and then run `sh ./get_theme.sh`
to download the theme.

<info>

`get_theme.sh` as you might have guessed is a shell script and is probably
incompatible windows, so you might have to use something like `gitbash`.

On a completely different note, only run the `get_theme.sh` script when
updating your outdated version of the theme or downloading it for the
first time.

</info>

To start a local server and preview changes run `mdbook serve -p [port]`
and open `http://localhost:[port]` in your browser.\
The `-p` flag is optional, the default is `3000`.

## How To Markdown

As you might have noticed we use markdown, pure markdown, not even mdx\
OFC we have some helper thingies with some code magic to make writing
documentation easier.\
But this also means, you must folloow some rules and note down some points.

### Markdown Rules

1. Use a (proper) markdown linter.
2. Follow basic markdown syntax.
3. Encapsulate links in `<` and `>`.
4. Make sure all html tags are closed appropriately.

### Some useful points

- The endpoints section is under the `endpoints` folder outside of `src`
  which contains yaml files, thats where all of the endpoint documentation
  goes.
- Make sure the documentation you write matches the format of the rest
  of the documentation, i.e no inconsistencies in the format.
- When writing critical pieces of information make sure that its valid.

<note>

If you have any queries or clarifications to be made, join the
*official* Unofficial Discord Documentation server!

<server id="zVB5P96GE2"></server>

</note>
