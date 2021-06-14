"""Functional test for the GildedRose."""
from gilded_rose import GildedRose, Item


def test_foo():
    """Test that item foo has correct name."""
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
