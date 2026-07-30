"""UEFN Virtual Pointer — Store desktop plugin (bundles the virtualpointer skill pack)."""

from __future__ import annotations


def register(api) -> None:
    """Skill-only pack: no MCP tools; register marks the plugin loaded."""
    api.log("virtualpointer skill plugin registered")
