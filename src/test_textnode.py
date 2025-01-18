import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_false(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_eq_false2(self):
        node1 = TextNode("<h1> hello world </h1/>", TextType.CODE)
        node2 = TextNode("<h2> hello world </h2/>", TextType.CODE)
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode("This is a text node",
                        TextType.CODE, "https://someurl.com")
        expected_repr = "TextNode(This is a text node, code, https://someurl.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_repr_without_url(self):
        node = TextNode("This is a text node",
                        TextType.CODE, )
        expected_repr = "TextNode(This is a text node, code, None)"
        self.assertEqual(repr(node), expected_repr)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE,
                        "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()
