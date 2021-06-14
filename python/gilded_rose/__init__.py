"""Init for the gilded rose."""

from gilded_rose import dtypes
from gilded_rose.updater import legacy


Item = dtypes.Item


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            legacy.update(item)
