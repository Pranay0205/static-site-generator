import unittest
from htmlnode import HTMLNODE


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html_standard(self):
        """Test conversion of standard link properties to HTML."""
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNODE("a", "Click me", None, props)
        result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), result)

    def test_props_to_html_empty_dict(self):
        """Test conversion of empty properties dictionary to HTML."""
        node = HTMLNODE("p", "Hello", None, {})
        result = ""
        self.assertEqual(node.props_to_html(), result)

    def test_props_to_html_multiple_attributes(self):
        """Test conversion of multiple HTML attributes."""
        props = {
            "class": "header",
            "id": "main-title",
            "data-test": "true"
        }
        node = HTMLNODE("h1", "Title", None, props)
        result = " class=\"header\" id=\"main-title\" data-test=\"true\""
        self.assertEqual(node.props_to_html(), result)

    def test_repr_with_standard_props(self):
        """Test HTMLNode representation with href and target properties."""
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNODE("a", "Click me", None, props)
        expected = "HTMLNODE(a, Click me, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(node), expected)

    def test_repr_nested_props(self):
        """Test HTMLNode representation with nested properties."""
        props = {
            "style": {
                "color": "red",
                "font-size": "14px"
            },
            "class": "header"
        }
        node = HTMLNODE("h1", "Title", None, props)
        expected = "HTMLNODE(h1, Title, None, {'style': {'color': 'red', 'font-size': '14px'}, 'class': 'header'})"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main()
