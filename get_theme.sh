#!/bin/bash

# Copyright 2022 한승민
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

rm -rf ./theme
mkdir ./theme
cd ./theme
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/book.js > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/highlight.js > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/highlight.css > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/index.hbs > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/redirect.hbs > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/favicon.png > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/favicon.svg > /dev/null 2>&1
mkdir ./css
cd ./css
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/css/variables.css > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/css/general.css > /dev/null 2>&1
wget --no-cache https://raw.githubusercontent.com/discord-undoc/discord-undoc-theme/master/theme/css/chrome.css > /dev/null 2>&1
cd ../../
