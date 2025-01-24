from enum import Enum
import re


class BlockType(Enum):
    paragraph = "paragraph",
    heading = "heading",
    code = "code",
    quote = "quote",
    unordered_list = "unordered_list",
    ordered_list = "ordered_list"


def block_to_block_type(markdown_block):
    paragraph_regex = r"^[^#>].*"  # paragraph
    heading_regex = r"^(#+) (.*)"  # heading
    code_regex = r"^```"  # code
    quote_regex = r"^>"  # quote
    unordered_list_regex = r"^\* "  # unordered_list
    ordered_list_regex = r"^\d+\. "  # ordered_list

    if re.match(heading_regex, markdown_block):
        return BlockType.heading
    if re.match(code_regex, markdown_block):
        return BlockType.code
    if re.match(quote_regex, markdown_block):
        return BlockType.quote
    if re.match(unordered_list_regex, markdown_block):
        return BlockType.unordered_list
    if re.match(ordered_list_regex, markdown_block):
        return BlockType.ordered_list
    if re.match(paragraph_regex, markdown_block):
        return BlockType.paragraph
    raise ValueError("Invalid markdown block")
