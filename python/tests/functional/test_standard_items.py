"""Functional test for standard items."""
from gilded_rose import GildedRose, Item


def test_foo():
    """Test that item foo has correct name."""
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"


def test_reduction():
    """Test that item quality and sell_in is reduced."""
    items = [Item("foo", 2, 2)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
    assert items[0].quality == 1
    assert items[0].sell_in == 1


def test_not_below_zero():
    """Test that item quality cannot go below 0."""
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
    assert items[0].quality == 0
    assert items[0].sell_in == -1


def test_reduction_negative_sell_in():
    """Test that item quality is reduce twice as fast if negative sell in."""
    items = [Item("foo", -1, 4)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
    assert items[0].quality == 2
    assert items[0].sell_in == -2
