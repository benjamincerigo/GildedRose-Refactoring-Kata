"""Test standard."""
from gilded_rose import Item

from gilded_rose.updater import standard


def test_reduction():
    """Test that item quality and sell_in is reduced."""
    item = Item("foo", 2, 2)
    r_item = standard.updater(1, item)
    assert r_item is item
    assert item.name == "foo"
    assert item.quality == 1
    assert item.sell_in == 1


def test_reduction_multiplier_2():
    """Test that item quality and sell_in is reduced by twice."""
    item = Item("foo", 2, 4)
    r_item = standard.updater(2, item)
    assert r_item is item
    assert item.name == "foo"
    assert item.quality == 2
    assert item.sell_in == 1


def test_not_below_zero():
    """Test that item quality cannot go below 0."""
    item = Item("foo", 2, 0)
    r_item = standard.updater(1, item)
    assert r_item is item
    assert item.name == "foo"
    assert item.quality == 0
    assert item.sell_in == 1


def test_not_below_zero_multiplier_2():
    """Test that item quality cannot go below 0."""
    item = Item("foo", 2, 0)
    r_item = standard.updater(2, item)
    assert r_item is item
    assert item.name == "foo"
    assert item.quality == 0
    assert item.sell_in == 1


def test_reduction_negative_sell_in():
    """Test that item quality is reduced twice as fast if negative sell in."""
    item = Item("foo", -1, 4)
    r_item = standard.updater(1, item)
    assert r_item is item
    assert item.name == "foo"
    assert item.quality == 2
    assert item.sell_in == -2


def test_reduction_negative_sell_in_multiplier_2():
    """Test that item quality is reduced twice as fast if negative sell in."""
    item = Item("foo", -1, 5)
    r_item = standard.updater(2, item)
    assert r_item is item
    assert item.name == "foo"
    assert item.quality == 1
    assert item.sell_in == -2

