import unittest

from title_extractor import extract_title


class test_title_extractor(unittest.TestCase):

    def test_single_heading(self):
        markdown = "# Heading 1"
        result = extract_title(markdown)

        self.assertEqual(result, "Heading 1")

    def test_multiline_title(self):
        markdown = "# Heading 1 \n continued text for headline"

        result = extract_title(markdown)

        self.assertEqual(result, "Heading 1 \n continued text for headline")

    def test_ignoring_lines_after_title(self):
        markdown = "# Heading 1\n\n some text after the title heading"

        result = extract_title(markdown)

        self.assertEqual(result, "Heading 1")

    def test_ignoring_second_hash_in_heading(self):
        markdown = "# Heading 1 # Should Ignore this hash"

        result = extract_title(markdown)

        self.assertEqual(result, "Heading 1 # Should Ignore this hash")

    def test_title_with_multiple_spaces(self):
        markdown = "#    Title    with    spaces    "
        self.assertEqual(extract_title(markdown), "Title    with    spaces")

    def test_empty_title(self):
        markdown = "# "
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_empty_string(self):
        markdown = ""
        with self.assertRaises(Exception):
            extract_title(markdown)
