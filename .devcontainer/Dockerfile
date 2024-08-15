FROM mcr.microsoft.com/devcontainers/python:3.12

ARG USERNAME=vscode

RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
&& mkdir /commandhistory \
&& touch /commandhistory/.bash_history \
&& chown -R ${USERNAME} /commandhistory \
&& echo "$SNIPPET" >> "/home/${USERNAME}/.bashrc"

USER vscode

RUN curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash
ENV PATH=${PATH}:/home/${USERNAME}/.rye/shims

CMD ["bash"]
