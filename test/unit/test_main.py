"""Test module for the cow greeting function."""

from src.main import cow_say


def test_cow_say():
    """Test the cow_say function."""
    assert cow_say() == "Moo! I'm a cow!"
