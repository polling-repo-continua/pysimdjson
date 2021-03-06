import pytest


def test_load(parser):
    """Ensure we can load from disk."""
    with pytest.raises(ValueError):
        parser.load('jsonexamples/invalid.json')

    doc = parser.load("jsonexamples/small/demo.json")
    doc.at('Image/Width')


def test_parse(parser):
    """Ensure we can load from string fragments."""
    parser.parse(b'{"hello": "world"}')
