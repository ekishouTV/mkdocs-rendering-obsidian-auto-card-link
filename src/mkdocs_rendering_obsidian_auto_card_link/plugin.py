import pkgutil
import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page


class RenderingObsidianAutoCardLink(BasePlugin):
    def __init__(self) -> None:
        super().__init__()

        self._pattern = re.compile(
            r"""
            ```cardlink\n
            url:\s(?P<url>.*)\n
            title:\s(?P<title>.*)\n
            description:\s(?P<description>.*)\n
            host:\s(?P<host>.*)\n
            favicon:\s(?P<favicon>.*)\n
            image:\s(?P<image>.*)\n
            ```
            """,
            re.VERBOSE,
        )

    def _generate_html(self, m: re.Match) -> str:
        card = self._template
        card = card.replace("{{ url }}", m.group("url"))
        card = card.replace("{{ title }}", m.group("title").replace('"', ""))
        card = card.replace("{{ description }}", m.group("description").replace('"', ""))
        card = card.replace("{{ favicon }}", m.group("favicon"))
        card = card.replace("{{ host }}", m.group("host"))
        card = card.replace("{{ image }}", m.group("image"))

        return card

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig | None:
        self._template = pkgutil.get_data(__name__, "assets/card.html").decode("utf-8")

        return config

    def on_page_markdown(self, markdown: str, /, *, page: Page, config: MkDocsConfig, files: Files) -> str | None:
        if "```cardlink" not in markdown:
            return None

        return self._pattern.sub(self._generate_html, markdown)
