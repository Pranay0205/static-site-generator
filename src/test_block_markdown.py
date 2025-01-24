import unittest
from block_markdown import BlockType, block_to_block_type
from inline_markdown import mark_down_blocks


class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_block(self):
        text = """# This is a heading

                    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                    * This is the first list item in a list block
                    * This is a list item
                    * This is another list item"""

        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
                    '* This is the first list item in a list block\n* This is a list item\n* This is another list item']

        actual = mark_down_blocks(text)

        self.assertEqual(expected, actual)

    def test_markdown_multiline_block(self):
        text = """# This is a heading

        

                    This is a paragraph of text. It has some **bold** and *italic* words inside of it.



                    * This is the first list item in a list block  
                    * This is a list item 
                    * This is another list item """

        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
                    '* This is the first list item in a list block\n* This is a list item\n* This is another list item']

        actual = mark_down_blocks(text)

        self.assertEqual(expected, actual)

    def test_block_to_block_type(self):
        actual = block_to_block_type("# This is a heading")
        expected = BlockType.heading
        self.assertEqual(expected, actual)

    def test_block_to_block_type_code(self):
        actual = block_to_block_type("```")
        expected = BlockType.code
        self.assertEqual(expected, actual)

    def test_block_to_block_type_quote(self):
        actual = block_to_block_type("> This is a quote")
        expected = BlockType.quote
        self.assertEqual(expected, actual)

    def test_block_to_block_type_unordered_list(self):
        actual = block_to_block_type("* This is a list item")
        expected = BlockType.unordered_list
        self.assertEqual(expected, actual)

    def test_block_to_block_type_ordered_list(self):
        actual = block_to_block_type("1. This is a list item")
        expected = BlockType.ordered_list
        self.assertEqual(expected, actual)

    def test_block_to_block_type_paragraph(self):
        actual = block_to_block_type("This is a paragraph of text")
        expected = BlockType.paragraph
        self.assertEqual(expected, actual)
