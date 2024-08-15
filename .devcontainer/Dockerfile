FROM mcr.microsoft.com/devcontainers/python:3.12

ARG USERNAME

RUN usermod -l ${USERNAME} -d "/home/${USERNAME}/" -m vscode && groupmod -n ${USERNAME} vscode \
    && usermod -aG sudo ${USERNAME} \
    && rm /etc/sudoers.d/vscode \
    && echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && mkdir /commandhistory \
    && touch /commandhistory/.bash_history \
    && chown -R ${USERNAME} /commandhistory \
    && echo "$SNIPPET" >> "/home/${USERNAME}/.bashrc"

USER ${USERNAME}

RUN curl -sSf https://rye.astral.sh/get | RYE_VERSION="0.42.0" RYE_INSTALL_OPTION="--yes" bash
ENV PATH=${PATH}:/home/${USERNAME}/.rye/shims

CMD ["bash"]
