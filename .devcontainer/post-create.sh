#!/bin/bash

rye sync

# Enable completion of Rye
sudo apt-get update
sudo apt-get -y install bash-completion
mkdir -p ~/.local/share/bash-completion/completions
rye self completion > ~/.local/share/bash-completion/completions/rye.bash

# Starship
mkdir ~/.local/bin
curl -sS https://starship.rs/install.sh | sh -s -- -y -b ~/.local/bin
touch ~/.config/starship.toml && ~/.local/bin/starship preset -o ~/.config/starship.toml gruvbox-rainbow
echo 'PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(starship init bash)"' >> ~/.bashrc
