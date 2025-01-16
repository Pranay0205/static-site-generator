import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_false(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
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


if __name__ == "__main__":
    unittest.main()
