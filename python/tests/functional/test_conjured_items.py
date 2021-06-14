"""Functional test for the Conjured Items."""
from gilded_rose import GildedRose, Item
from gilded_rose.updater import constants


def test_reduction():
    """Test that item quality and sell_in is reduce."""
    items = [Item(constants.CONJURED_KEY, 2, 3)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == constants.CONJURED_KEY
    assert items[0].quality == 1
    assert items[0].sell_in == 1


def test_not_below_zero():
    """Test that item quality cannot go below 0."""
    items = [Item(constants.CONJURED_KEY, 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == constants.CONJURED_KEY
    assert items[0].quality == 0
    assert items[0].sell_in == -1


def test_reduction_negative_sell_in():
    """Test that item quality is reduce twice as fast if negative sell in."""
    items = [Item(constants.CONJURED_KEY, -1, 5)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == constants.CONJURED_KEY
    assert items[0].quality == 1
    assert items[0].sell_in == -2
