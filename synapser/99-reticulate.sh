#!/bin/sh

# The synapser package requires r-reticulate python environment and will
# build one if it isn't present. This code creates a symlink to a pre-installed
# venv if one doesn't already exist in the user's home directory.

symlink_dir="$HOME/.virtualenvs/r-reticulate"

if [ ! -d "$symlink_dir" ] && [ ! -L "$symlink_dir" ]; then
    
    if [ ! -d "$HOME/.virtualenvs" ]; then
        mkdir "$HOME/.virtualenvs"
    fi
    
    ln -s /root/.virtualenvs/r-reticulate "$symlink_dir"
fi
