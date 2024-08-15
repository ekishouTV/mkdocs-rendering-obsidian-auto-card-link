#!/bin/bash

rye sync

# Enable Git signed commit via SSH
git config gpg.format ssh
git config user.signingkey ~/.ssh/id_ed25519.pub
git config commit.gpgsign true

# Enable completion of Rye
sudo apt-get update
sudo apt-get -y install bash-completion
mkdir -p ~/.local/share/bash-completion/completions
rye self completion > ~/.local/share/bash-completion/completions/rye.bash

# Starship
mkdir ~/.local/bin
curl -sS https://starship.rs/install.sh | sh -s -- -y -b ~/.local/bin
echo 'PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(starship init bash)"' >> ~/.bashrc
