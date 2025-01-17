import unittest
from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        """Test that ParentNode.to_html() correctly renders nested HTML elements."""
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_recursion(self):
        """Test that ParentNode.to_html() recursively renders nested HTML elements."""
        node = ParentNode(
            "p",
            [
                ParentNode("p", [LeafNode("b", "Bold text"), ParentNode(
                    "p", [LeafNode("i", "Pranay Ghuge")])]),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        expected_html = "<p><p><b>Bold text</b><p><i>Pranay Ghuge</i></p></p>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_deep_nesting(self):
        """Test HTML rendering with deep nested structure."""
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "article",
                            [
                                LeafNode("h1", "Title"),
                                ParentNode(
                                    "p",
                                    [LeafNode("em", "Important"),
                                     LeafNode(None, " message")]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
        expected = "<div><section><article><h1>Title</h1><p><em>Important</em> message</p></article></section></div>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_mixed_props(self):
        """Test HTML rendering with properties at different nesting levels."""
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "nav",
                    [LeafNode("a", "Link")]
                ),
                ParentNode(
                    "main",
                    [
                        LeafNode("h1", "Title", {"id": "header"}),
                        LeafNode(None, "Text")
                    ]
                )
            ]
        )
        expected = '<div><nav><a>Link</a></nav><main><h1>Title</h1>Text</main></div>'
        self.assertEqual(node.to_html(), expected)
