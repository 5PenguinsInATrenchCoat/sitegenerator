import unittest

from htmlnode import HTMLNode


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



if __name__ == "__main__":
    unittest.main()