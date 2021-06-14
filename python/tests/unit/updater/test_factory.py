"""Test updater factory."""
import mock

from gilded_rose import dtypes
from gilded_rose.updater import constants, factory


def test_not_found():
    """Test item with no updater."""
    item = dtypes.Item("not_found", 1, 1)
    result = factory.get_updater(item)
    assert result is None


@mock.patch("gilded_rose.updater.factory.create_conjured_updater")
def test_conjured(m_create_conjured_updater):
    """Test that create_conjured_updater is called for Conjured items."""
    item = dtypes.Item(constants.CONJURED_KEY, 1, 1)
    result = factory.get_updater(item)
    m_create_conjured_updater.assert_called_once()
    assert result is m_create_conjured_updater.return_value


@mock.patch("gilded_rose.updater.standard.updater")
def test_create_conjured_updater(m_standard_updater):
    """Test create_conjured_updater."""
    item = dtypes.Item("f", 1, 1)
    r = factory.create_conjured_updater()
    assert r
    r(item)
    m_standard_updater.assert_called_once_with(2, item)
