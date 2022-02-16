if [[ $1 == publish:* ]]
then
    echo "Preparing to download mdbook..."
    curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh
    cargo install mdbook > /dev/null 2>&1
    echo "Cloning repository..."
    git clone https://github.com/discord-undoc/discord-undoc.github.io.git --branch master master > /dev/null 2>&1
    git clone https://github.com/discord-undoc/discord-undoc.github.io.git --branch gh-pages ghpages > /dev/null 2>&1
    git config --global user.name $3
    git config --global user.email $4
    cd master
    chmod +x get_theme.sh
    echo "Installing dependencies..."
    curl -sSL https://install.python-poetry.org | python -
    $HOME/.local/bin/poetry install
    $HOME/.local/bin/poetry shell
    echo "Getting latest theme..."
    ./get_theme.sh
    echo "Building book..."
    mdbook build > /dev/null 2>&1
    echo "Copying to gh-pages branch..."
    rm -rf ../ghpages/*
    cp -r ./book/* ../ghpages > /dev/null 2>&1
    cd ../ghpages
    git remote set-url origin https://x-access-token:$2@github.com/$GITHUB_REPOSITORY > /dev/null 2>&1
    git add . > /dev/null 2>&1
    git commit -m "[ $3 ] Automated deploy - $5" > /dev/null 2>&1
    echo "Pushing to gh-pages branch..."
    git push origin gh-pages > /dev/null 2>&1
    echo "Successfully deployed documentation!"
else
    echo "Not a deploy commit! Ignoring..."
fi