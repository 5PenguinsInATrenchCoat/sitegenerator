import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_differing_text(self):
        node = TextNode("This is the second test", TextType.ITALIC)
        node2 = TextNode("This isn't the second test", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_matching(self):
        node = TextNode("This test contains a link", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This test contains a link", TextType.LINK, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_single_url(self):
        node = TextNode("This test may contain a link", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This test may contain a link", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_dif_texttypes(self):
        node = TextNode("This test has varied text types", TextType.BOLD)
        node2 = TextNode("This test has varied text types", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    
if __name__ == "__main__":
    unittest.main()
