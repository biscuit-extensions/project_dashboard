from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class ProjectDashboard(Extension):
    """Project overview with git status, recent files, and stats"""

    def __init__(self, api: "ExtensionsAPI") -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("Project Dashboard extension initialised.")

    def install(self) -> None:
        """Run when extension is loaded."""
        self.api.logger.info("Project Dashboard installed successfully.")
