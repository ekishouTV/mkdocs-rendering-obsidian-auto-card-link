#!/bin/bash

rye sync

# Enable completion of Rye
sudo apt-get update
sudo apt-get -y install bash-completion
mkdir -p ~/.local/share/bash-completion/completions
rye self completion > ~/.local/share/bash-completion/completions/rye.bash
