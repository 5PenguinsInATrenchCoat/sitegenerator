import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a BOLD node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a BOLD node")

    def test_img(self):
        node = TextNode("This is a img node", TextType.IMAGE, "image.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "image.com")
        self.assertEqual(html_node.props["alt"], "This is a img node")

    

    
if __name__ == "__main__":
    unittest.main()
