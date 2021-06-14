"""Factory for the updates."""
from typing import Optional

from functools import partial

from gilded_rose import dtypes
from gilded_rose.updater import constants, standard, utils


def get_updater(item: dtypes.Item) -> Optional[utils.Updater]:
    """Get the updater for the item."""
    if item.name == constants.CONJURED_KEY:
        return create_conjured_updater()

    return None


def create_conjured_updater() -> utils.Updater:
    """Create the updater for conjured items."""
    return partial(standard.updater, 2)
