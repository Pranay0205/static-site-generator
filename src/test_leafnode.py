import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_init_with_required_value(self):
        # Test that initialization works with just a value
        node = LeafNode(value="Hello")
        self.assertEqual(node.value, "Hello")
        self.assertIsNone(node.tag)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_all_parameters(self):
        # Test initialization with all parameters
        node = LeafNode(
            tag="span",
            value="Hello",
            props={"class": "greeting", "id": "hello-text"}
        )
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Hello")
        self.assertIsNone(node.children)
        self.assertEqual(node.props, {"class": "greeting", "id": "hello-text"})

    def test_to_html_without_tag(self):
        # Test HTML generation for node without tag
        node = LeafNode(value="Hello World")
        self.assertEqual(node.to_html(), "Hello World")

    def test_to_html_with_tag_no_props(self):
        # Test HTML generation with tag but no properties
        node = LeafNode(tag="p", value="Hello World")
        self.assertEqual(node.to_html(), "<p>Hello World</p>")

    def test_to_html_with_tag_and_props(self):
        # Test HTML generation with tag and properties
        node = LeafNode(
            tag="a",
            value="Click me",
            props={"href": "https://example.com", "class": "link"}
        )
        expected = '<a href="https://example.com" class="link">Click me</a>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_special_characters(self):
        # Test HTML generation with special characters in value
        node = LeafNode(tag="p", value="Hello & Goodbye")
        self.assertEqual(node.to_html(), "<p>Hello & Goodbye</p>")


if __name__ == '__main__':
    unittest.main()
