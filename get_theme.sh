#!/bin/bash

rm -rf ./theme
mkdir ./theme
cd ./theme
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/discord_undoc.py > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/book.js > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/highlight.js > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/highlight.css > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/index.hbs > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/favicon.png > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/favicon.svg > /dev/null 2>&1
mkdir ./css
cd ./css
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/css/variables.css > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/css/general.css > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/css/chrome.css > /dev/null 2>&1
cd ../../
