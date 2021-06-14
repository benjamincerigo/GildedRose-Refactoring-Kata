"""Legacy updater."""
from gilded_rose import dtypes


# This function is being removed from the linting
# As it is legacy and should be refactored out step by step
def update(item: dtypes.Item) -> dtypes.Item:  # noqa: C901
    """Update item using legacy functionality."""
    if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
        if item.quality > 0:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = item.quality - 1
    else:
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in < 11:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.sell_in < 6:
                    if item.quality < 50:
                        item.quality = item.quality + 1
    if item.name != "Sulfuras, Hand of Ragnaros":
        item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        if item.name != "Aged Brie":
            if item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                item.quality = item.quality - item.quality
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
    return item
