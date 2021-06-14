"""Functional test for the GildedRose."""
from gilded_rose import GildedRose, Item


def test_foo():
    """Test that item foo has correct name."""
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"


def test_standard_reduction():
    """Test that item quality and sell_in is reduce"""
    items = [Item("foo", 2, 2)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
    assert items[0].quality == 1
    assert items[0].sell_in == 1
