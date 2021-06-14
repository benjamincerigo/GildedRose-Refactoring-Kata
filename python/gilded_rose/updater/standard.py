"""Standard Updater."""
from gilded_rose import dtypes


def updater(multiplier: int, item: dtypes.Item) -> dtypes.Item:
    """Standard Updater with a multiplier."""
    item.sell_in = item.sell_in - 1

    if item.quality <= 0:
        return item

    if item.sell_in < 0:
        item.quality = item.quality - (2 * multiplier)
        return item

    item.quality = item.quality - (1 * multiplier)
    return item
