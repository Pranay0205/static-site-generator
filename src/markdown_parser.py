from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes
from textnode import TextType, text_node_to_html_node


def create_html_heading(text):
    level = text.count("#")
    return HTMLNode(f"h{level}", text.strip("# "))


def text_to_children(block):
    htmlnodes = []
    for line in block.split("\n"):
        parentnode = None
        textnodes = text_to_textnodes(line)
        for textnode in textnodes:
            if textnode.text.startswith("#"):
                parentnode = create_html_heading(textnode.text)
            else:
                htmlnode = text_node_to_html_node(textnode)
                parentnode.children = htmlnode

    return [parentnode]


def markdown_to_paragraph_node(markdown):
    htmlnode = HTMLNode("p", markdown)
    # print(htmlnode)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.heading:
            text_to_children(block)
        if block_type == BlockType.paragraph:
            markdown_to_paragraph_node(block)


markdown_to_html_node("""## This is a **heading**\n\n### This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item""")
