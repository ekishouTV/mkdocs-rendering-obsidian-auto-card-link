from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page


class RenderingObsidianAutoCardLink(BasePlugin):
    def __init__(self) -> None:
        super().__init__()

    def on_page_markdown(self, markdown: str, /, *, page: Page, config: MkDocsConfig, files: Files) -> str | None:
        return "# RenderingObsidianAutoCardLink"
