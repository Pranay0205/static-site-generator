from enum import Enum
import re


class BlockType(Enum):
    paragraph = "paragraph",
    heading = "heading",
    code = "code",
    blockquote = "blockquote",
    unordered_list = "unordered_list",
    ordered_list = "ordered_list"


def markdown_to_blocks(text):
    markdown_blocks_unfiltered = text.split("\n\n")
    blocks = []

    for block in markdown_blocks_unfiltered:
        if block.strip():
            if "\n" in block:
                cleaned_line = [line.strip() for line in block.split("\n")]
                blocks.append("\n".join(cleaned_line))
            else:
                blocks.append(block.strip())

    return blocks


def check_order(block):
    if block[0] != "1":
        raise ValueError("Ordered list does not in order")
    prev = 0
    for item in block.split("\n"):
        if int(item[0]) != prev + 1:
            ValueError("Order has miss order")
        prev = int(item[0])
    return True


def block_to_block_type(markdown_block):
    heading_regex = r"^(#{1,6}) (.*)"  # heading
    code_regex = r"^```[\s\S]*```\s*$"
    quote_regex = r"^>"  # quote
    unordered_list_regex = r"^(?:\* |\- )"  # unordered_list
    ordered_list_regex = r"^\d+\. "  # ordered_list

    if re.match(heading_regex, markdown_block):
        return BlockType.heading
    if re.match(code_regex, markdown_block):
        return BlockType.code
    if re.match(quote_regex, markdown_block):
        return BlockType.blockquote
    if re.match(unordered_list_regex, markdown_block):
        return BlockType.unordered_list
    if re.match(ordered_list_regex, markdown_block):
        if check_order(markdown_block):
            return BlockType.ordered_list
        ValueError("Invalid Ordered List")
    return BlockType.paragraph
