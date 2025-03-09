import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode



class TestHTMLNode(unittest.TestCase):
    def test_basic(self):
        node = HTMLNode(
            tag="a",
            value="some value",
            props={
                "href": "https://www.google.com"
            }
        )
        output = node.props_to_html()
        self.assertIn(' href="https://www.google.com"', output)

    def test_multiple_props(self):
        node = HTMLNode(
            props={
                "href": "https://www.youtube.com",
                "prop": "another prop"
            }
        )
        output = node.props_to_html()
        self.assertIn(' href="https://www.youtube.com"', output)
        self.assertIn(' prop="another prop"', output)

    def test_no_props(self):
        node = HTMLNode(
            tag="b",
            value="no props here"
        )
        output = node.props_to_html()
        self.assertEqual('', output)

class TestLeafNode(unittest.TestCase):
    def test_basic(self):
        node = LeafNode(
            tag=None,
            value="hello world"
        )
        output = node.to_html()
        self.assertEqual("hello world", output)

    def test_no_props(self):
        node = LeafNode(
            tag="p",
            value="hello world"
        )
        output = node.to_html()
        self.assertEqual("<p>hello world</p>", output)

    def test_with_props(self):
        node = LeafNode(
            tag="a",
            value="hello world",
            props={
                "href": "google.com",
                "class": "link"
            }
        )
        output = node.to_html()
        self.assertEqual('<a href="google.com" class="link">hello world</a>', output)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode(
                tag="q",
                props={
                    "href": "youtube.com"
                }
            )
            node.to_html()




if __name__ == "__main__":
    unittest.main()