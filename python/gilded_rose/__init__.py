"""Init for the gilded rose."""

from gilded_rose import dtypes
from gilded_rose.updater import factory, legacy


Item = dtypes.Item


class GildedRose(object):
    """GildedRose interface."""

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """Update the items."""
        for item in self.items:
            updater = factory.get_updater(item)
            if updater:
                updater(item)
            else:
                legacy.update(item)
