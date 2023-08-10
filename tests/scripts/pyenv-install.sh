#!/bin/bash

# This script installs pyenv and all selected python versions

# Get script dir
dir="$(cd "$(dirname "$0")" && pwd)"
filterScript="$dir/filter-python-versions.py"

# Pyenv isntall and init
curl https://pyenv.run | bash
echo 'export PATH="$PATH:$HOME/.pyenv/bin"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
export PATH="$PATH:$HOME/.pyenv/bin"
eval "$(pyenv virtualenv-init -)"

for version in $(pyenv install --list | python3 $filterScript); do
    echo "=> Installing python version: $version"
    pyenv install $version
done
