"""Updater utils."""
from typing_extensions import Protocol

from gilded_rose import dtypes


class Updater(Protocol):
    """Protocol for an Updater."""

    def __call__(self, item: dtypes.Item) -> dtypes.Item:
        """Protocol for an Updater."""
        ...
