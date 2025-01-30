import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from markdown_parser import (
    parse_heading,
    parse_paragraph,
    parse_unordered_list,
    parse_ordered_list,
    parse_blockquote,
    parse_codeblock,
    markdown_to_html_node
)


class TestParseHeading(unittest.TestCase):
    def test_single_heading(self):
        block = "# Heading 1"
        result = parse_heading(block)

        self.assertEqual(len(result), 1)

        node = result[0]
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.children.value, "Heading 1")

    def test_multiple_headings(self):
        block = "# Heading 1\n## Heading 2"
        result = parse_heading(block)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].tag, "h1")
        self.assertEqual(result[1].tag, "h2")
        self.assertEqual(result[0].children.value, "Heading 1")
        self.assertEqual(result[1].children.value, "Heading 2")

    def test_paragrph(self):
        block = "This is a paragraph with multiple lines.\nWhich should get parsed"

        result = parse_paragraph(block)

        print(result)


if __name__ == '__main__':
    unittest.main()
